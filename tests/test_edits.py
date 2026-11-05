"""rename-id and split-topic: correct references, history, and nothing written on failure."""

import pytest
from typer.testing import CliRunner

from conftest import add, course, topic
from kg.checks import run_checks
from kg.cli import app
from kg.edits import EditError, apply_edit, rename_id, split_topic
from kg.graph import KnowledgeGraph
from kg.model import Course
from kg.store import load_graph, write_graph

runner = CliRunner()
EVAL = "math.alg1.evaluate-expressions"
COMBINE = "math.alg1.combine-like-terms"
NEW = "math.alg1.evaluate-multivariable"


def snapshot(root):
    return {p: p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


def errors(kg):
    return [i for i in run_checks(kg) if i.severity == "error"]


def view_graph():
    kg = KnowledgeGraph()
    kg.courses = {
        "math.a": course("math.a", 3),
        "math.v": Course(
            id="math.v",
            subject="math",
            levels=("g4", "g6"),
            budget=0,
            view_topics=["math.a.one", "math.a.two"],
        ),
    }
    add(
        kg,
        topic("math.a.one", level="gk"),
        topic("math.a.two", ["math.a.one"], keys=["math.a.one"], level="g4"),
        topic(
            "math.a.three",
            ["math.a.two"],
            keys=["math.a.two", "math.a.one"],
            encompassed=["math.a.one"],
        ),
    )
    return kg


def test_rename_updates_every_reference():
    kg = view_graph()
    new = rename_id(kg, "math.a.one", "math.a.zero")
    assert "math.a.one" not in new.topics and new.topics["math.a.zero"].id == "math.a.zero"
    assert list(new.topics)[0] == "math.a.zero"  # course order kept
    two, three = new.topics["math.a.two"], new.topics["math.a.three"]
    assert two.prerequisites[0].topic == "math.a.zero"
    assert two.knowledge_points[0].key_prerequisites == ["math.a.zero"]
    assert three.encompassed[0].topic == "math.a.zero"
    assert "math.a.zero" in three.knowledge_points[0].key_prerequisites
    assert new.courses["math.v"].view_topics == ["math.a.zero", "math.a.two"]
    assert not errors(new)
    assert "math.a.one" in kg.topics and kg.history == []  # input untouched


def test_rename_records_history():
    new = rename_id(view_graph(), "math.a.one", "math.a.zero")
    assert [(h.op, h.source, h.targets) for h in new.history] == [
        ("rename", "math.a.one", ["math.a.zero"])
    ]


def test_rename_to_existing_id_writes_nothing(sample_copy):
    before = snapshot(sample_copy)
    result = runner.invoke(app, ["rename-id", EVAL, COMBINE, "--root", str(sample_copy)])
    assert result.exit_code == 1 and "already exists" in result.output
    assert snapshot(sample_copy) == before
    with pytest.raises(EditError):
        rename_id(load_graph(sample_copy), EVAL, COMBINE)


def test_rename_cli_writes_and_history_persists(sample_copy):
    result = runner.invoke(
        app, ["rename-id", EVAL, "math.alg1.evaluate-algebraic", "--root", str(sample_copy)]
    )
    assert result.exit_code == 0, result.output
    kg = load_graph(sample_copy)
    assert "math.alg1.evaluate-algebraic" in kg.topics and EVAL not in kg.topics
    assert kg.history[-1].op == "rename"
    assert not errors(kg)


def split_sample(kg):
    return split_topic(
        kg,
        EVAL,
        NEW,
        "Evaluating multivariable expressions",
        move_kps=["kp3"],
        keep_new_kps=["Evaluate with a negative value"],
        new_kps=["Evaluate with fractions", "Evaluate nested expressions"],
    )


def test_split_moves_kps_and_repoints_dependents(sample_graph):
    new = split_sample(sample_graph)
    orig, moved = new.topics[EVAL], new.topics[NEW]
    assert [k.id for k in orig.knowledge_points] == ["kp1", "kp2", "kp4"]
    assert [k.id for k in moved.knowledge_points] == ["kp3", "kp5", "kp6"]
    order = list(new.topics)
    assert order.index(NEW) == order.index(EVAL) + 1
    assert [(e.topic, e.encompassing, e.confidence) for e in moved.prerequisites] == [
        (EVAL, 0.5, "low")
    ]
    assert [(e.topic, e.confidence) for e in moved.encompassed] == [
        ("math.arith.add-whole-numbers", "low")  # kp3's key prerequisite, weighted on the new topic
    ]
    dep = new.topics[COMBINE]
    assert [e.topic for e in dep.prerequisites] == [NEW]
    assert dep.knowledge_points[0].key_prerequisites == [NEW]
    assert sample_graph.topics[COMBINE].prerequisites[0].topic == EVAL  # input untouched
    assert [(h.op, h.source) for h in new.history] == [("split", EVAL)]


def test_split_result_validates(sample_graph):
    assert not errors(split_sample(sample_graph))


def test_split_marks_changed_edges_low_confidence(sample_graph):
    new = split_sample(sample_graph)
    repointed = [
        e
        for t in new.topics.values()
        if t.id != NEW
        for e in t.prerequisites + t.encompassed
        if e.topic == NEW
    ]
    assert repointed and all(e.confidence == "low" for e in repointed)
    # edges that were not touched keep their confidence
    assert new.topics[EVAL].prerequisites == sample_graph.topics[EVAL].prerequisites


def test_split_leaving_one_kp_writes_nothing_and_exits_1(sample_copy):
    before = snapshot(sample_copy)
    result = runner.invoke(
        app,
        [
            "split-topic",
            EVAL,
            "--new-id",
            "math.alg1.evaluate-more",
            "--new-name",
            "More",
            "--move-kps",
            "kp2,kp3",
            "--root",
            str(sample_copy),
        ],
    )
    assert result.exit_code == 1 and "kp-count" in result.output
    assert snapshot(sample_copy) == before


def test_split_three_kp_topic_with_added_kps_validates(sample_copy):
    result = runner.invoke(
        app,
        [
            "split-topic",
            EVAL,
            "--new-id",
            NEW,
            "--new-name",
            "Evaluating multivariable expressions",
            "--move-kps",
            "kp3",
            "--keep-kp",
            "Evaluate with a negative value",
            "--new-kp",
            "Evaluate with fractions",
            "--new-kp",
            "Evaluate nested expressions",
            "--root",
            str(sample_copy),
        ],
    )
    assert result.exit_code == 0, result.output
    kg = load_graph(sample_copy)
    assert len(kg.topics[EVAL].knowledge_points) == 3
    assert len(kg.topics[NEW].knowledge_points) == 3
    assert not errors(kg)
    assert runner.invoke(app, ["validate", "--root", str(sample_copy)]).exit_code == 0


def test_kp_ids_stay_stable_after_inserting(sample_graph):
    new = split_sample(sample_graph)
    old = {k.id: k.can_do for k in sample_graph.topics[EVAL].knowledge_points}
    after = {k.id: k.can_do for t in (EVAL, NEW) for k in new.topics[t].knowledge_points}
    for kid, text in old.items():
        assert after[kid] == text
    assert len(after) == 6  # no ID reused


def test_split_unknown_kp_or_clashing_id_raises(sample_graph):
    with pytest.raises(EditError):
        split_topic(sample_graph, EVAL, "math.alg1.x", "X", move_kps=["kp9"])
    with pytest.raises(EditError):
        split_topic(sample_graph, EVAL, COMBINE, "X", move_kps=["kp3"])


def test_apply_edit_returns_errors_and_writes_nothing(sample_copy):
    kg = load_graph(sample_copy)
    before = snapshot(sample_copy)
    bad = split_topic(kg, EVAL, "math.alg1.evaluate-more", "More", move_kps=["kp2", "kp3"])
    assert any(i.rule == "kp-count" for i in apply_edit(bad))
    assert snapshot(sample_copy) == before


def test_write_graph_empties_course_file_that_lost_all_topics(sample_copy):
    kg = load_graph(sample_copy)
    for tid in [t for t in kg.topics if t.startswith("physics.mech.")]:
        del kg.topics[tid]
    write_graph(kg)
    assert "topics: []" in (sample_copy / "physics" / "mech.yaml").read_text(encoding="utf-8")
    assert not [t for t in load_graph(sample_copy).topics if t.startswith("physics.mech.")]
