"""Stats, review reports, review queue and duplicate detection."""

import time

import pytest
from typer.testing import CliRunner

from conftest import add, course, edge, stub, topic, valid_graph
from kg.cli import app
from kg.graph import KnowledgeGraph
from kg.model import Edge, KnowledgePoint, Topic
from kg.reports import QueueItem, find_duplicates, review_queue, review_report, stats
from kg.store import write_graph
from kg.synthetic import generate


def with_conf(t: Topic, **by_target: str) -> Topic:
    t.prerequisites = [
        Edge(topic=e.topic, encompassing=e.encompassing, confidence=by_target.get(e.topic, "high"))
        for e in t.prerequisites
    ]
    return t


def test_stats_counts_match_a_known_graph():
    s = stats(valid_graph())
    assert s["topics"] == 4
    assert s["by_subject"] == {"math": 4}
    assert s["by_course"] == {"math.a": 3, "math.b": 1}
    assert s["by_level"] == {"gk": 1, "g4": 1, "g5": 1, "g6": 1}
    assert s["prerequisite_count"] == {0: 1, 1: 3}
    assert s["kp_count"] == {3: 4}
    assert s["depth"] == {0: 1, 1: 1, 2: 1, 3: 1}
    assert s["weight"]["count"] == 4 and s["weight"]["mean"] == pytest.approx(0.45)
    assert s["confidence_by_course"]["math.a"] == {"high": 3, "medium": 0, "low": 0}
    assert s["budget_variance"] == {"math.a": 0, "math.b": 0}


def test_stats_budget_variance_and_course_filter():
    kg = valid_graph()
    kg.courses["math.a"].budget = 5
    s = stats(kg)
    assert s["budget_variance"]["math.a"] == -2
    only = stats(kg, course="math.b")
    assert only["topics"] == 1 and only["by_course"] == {"math.b": 1}


def cross_graph() -> KnowledgeGraph:
    kg = valid_graph()
    kg.courses["physics.p"] = course("physics.p", 1, ["math.a"])
    add(kg, topic("physics.p.kin", ["math.a.two"], keys=["math.a.two"], level="g6"))
    return kg


def test_cross_subject_derived_from_subject_fields():
    rep = review_report(cross_graph())
    assert rep["cross_subject"] == [("physics.p.kin", "math.a.two", "direct")]
    assert review_report(valid_graph())["cross_subject"] == []


def encompassed_graph() -> KnowledgeGraph:
    """physics.p.kin lists math.a.one as an encompassed edge: low confidence and cross-subject."""
    kg = cross_graph()
    kin = kg.topics["physics.p.kin"]
    kin.encompassed = [Edge(topic="math.a.one", encompassing=0.4, confidence="low")]
    return kg


def test_report_and_queue_include_encompassed_edges_labelled_by_kind():
    kg = encompassed_graph()
    rep = review_report(kg)
    assert ("physics.p.kin", "math.a.one", "encompassed") in rep["low_confidence"]
    assert ("physics.p.kin", "math.a.one", "encompassed") in rep["cross_subject"]
    assert ("physics.p.kin", "math.a.two", "direct") in rep["cross_subject"]
    items = {(q.topic, q.prerequisite, q.kind) for q in review_queue(kg)}
    assert ("physics.p.kin", "math.a.one", "encompassed") in items
    assert ("physics.p.kin", "math.a.two", "direct") in items
    enc = next(q for q in review_queue(kg) if q.kind == "encompassed")
    assert enc.confidence == "low" and enc.cross_subject


def test_stats_weights_and_confidence_include_encompassed_edges():
    s = stats(valid_graph())  # three direct edges at 0.5, one encompassed at 0.3
    assert s["weight"]["count"] == 4
    assert s["weight"]["min"] == pytest.approx(0.3)
    assert s["confidence_by_course"]["math.a"]["high"] == 3


def test_cli_prints_encompassed_kind(tmp_path):
    root = tmp_path / "g"
    kg = encompassed_graph()
    kg.root = root
    write_graph(kg)
    out = CliRunner().invoke(app, ["review-queue", "--root", str(root)]).output
    assert any("physics.p.kin <- math.a.one" in ln and "encompassed" in ln for ln in out.splitlines())
    out = CliRunner().invoke(app, ["review-report", "--root", str(root)]).output
    assert "physics.p.kin <- math.a.one (encompassed)" in out


def test_queue_order():
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 6), "physics.p": course("physics.p", 1)}
    add(
        kg,
        topic("math.a.root"),
        with_conf(topic("math.a.m1", ["math.a.root"]), **{"math.a.root": "low"}),
        with_conf(topic("math.a.m2", ["math.a.root"]), **{"math.a.root": "low"}),
        topic("math.a.m3", ["math.a.m1"]),
        topic("math.a.m4", ["math.a.m1"]),
        with_conf(topic("math.a.m5", ["math.a.m2"]), **{"math.a.m2": "medium"}),
        with_conf(topic("physics.p.z", ["math.a.m2"]), **{"math.a.m2": "medium"}),
    )
    order = [(q.topic, q.prerequisite) for q in review_queue(kg)]
    assert order == [
        ("math.a.m1", "math.a.root"),  # low, 2 descendants
        ("math.a.m2", "math.a.root"),  # low, 2 descendants, later id
        ("physics.p.z", "math.a.m2"),  # not low, 0 descendants, cross-subject first
        ("math.a.m3", "math.a.m1"),  # then plain id order
        ("math.a.m4", "math.a.m1"),
        ("math.a.m5", "math.a.m2"),
    ]
    first = review_queue(kg)[0]
    assert isinstance(first, QueueItem) and first.descendants == 2 and not first.cross_subject
    assert review_queue(kg)[2].cross_subject
    assert [q.topic for q in review_queue(kg, limit=1)] == ["math.a.m1"]


def test_find_duplicates_flags_same_skill_in_two_courses():
    kg = KnowledgeGraph()
    a = topic("math.a.frac", level="g4")
    b = topic("math.b.frac", level="g5")
    a.name = b.name = "Adding fractions with unlike denominators"
    c = topic("math.b.other", level="g5")
    c.name = "Graphing parabolas"
    for t in (a, b, c):
        for kp in t.knowledge_points:
            kp.can_do = "Add two fractions"
    add(kg, a, b, c)
    assert find_duplicates(kg) == [("math.a.frac", "math.b.frac", 1.0)]


def test_find_duplicates_ignores_same_course_and_unrelated():
    kg = KnowledgeGraph()
    a, b, c = topic("math.a.x"), topic("math.a.y"), topic("math.b.z")
    a.name = b.name = "Adding fractions"
    c.name = "Graphing parabolas"
    for t in (a, b, c):
        for kp in t.knowledge_points:
            kp.can_do = "Do it"
    add(kg, a, b, c, stub("math.b.s", "Adding fractions"))
    assert find_duplicates(kg) == []


def test_reports_handle_empty_graph():
    kg = KnowledgeGraph()
    s = stats(kg)
    assert s["topics"] == 0 and s["by_course"] == {} and s["depth"] == {}
    assert review_report(kg) == {"low_confidence": [], "near_limits": [], "cross_subject": []}
    assert review_queue(kg) == [] and find_duplicates(kg) == []


def test_cli_reports_print_text(tmp_path):
    root = tmp_path / "g"
    write_graph(generate(60, seed=2, root=root))
    runner = CliRunner()
    for cmd in (["stats"], ["review-report"], ["review-queue", "--limit", "3"], ["find-duplicates"]):
        res = runner.invoke(app, [*cmd, "--root", str(root)])
        assert res.exit_code == 0, res.output
    res = runner.invoke(app, ["stats", "--root", str(root), "--course", "math.c01"])
    assert res.exit_code == 0 and "math.c01" in res.output
    res = runner.invoke(app, ["review-queue", "--limit", "3", "--root", str(root)])
    assert len(res.output.strip().splitlines()) <= 3


def test_find_duplicates_under_30_seconds_on_20000_topics():
    kg = generate(20000, seed=3)
    start = time.perf_counter()
    result = find_duplicates(kg)
    assert time.perf_counter() - start < 30
    assert isinstance(result, list)
