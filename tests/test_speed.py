"""Synthetic-graph validity, density and the validate speed budget."""

import time

from kg.checks import run_checks
from kg.store import load_graph, write_graph
from kg.synthetic import generate


def errors(issues):
    return [i for i in issues if i.severity == "error"]


def mean_kps(kg):
    return sum(len(t.knowledge_points) for t in kg.topics.values()) / len(kg.topics)


def mean_weighted_edges(kg):
    return sum(len(t.prerequisites) + len(t.encompassed) for t in kg.topics.values()) / len(
        kg.topics
    )


def test_synthetic_graph_has_no_errors_and_hits_density():
    kg = generate(2000, seed=1)
    assert not errors(run_checks(kg))
    assert 3.2 <= mean_kps(kg) <= 3.6 and 4.5 <= mean_weighted_edges(kg) <= 5.5


def test_synthetic_is_deterministic_and_sized():
    a, b = generate(500, seed=3), generate(500, seed=3)
    assert a.topics == b.topics and a.courses == b.courses
    assert len(a.topics) == 500
    assert {c.subject for c in a.courses.values()} == {
        "math", "physics", "chemistry", "biology", "engineering"
    }
    for c in a.courses.values():
        assert c.budget == sum(1 for t in a.topics.values() if t.course_id == c.id)


def test_synthetic_fits_layout_limits():
    kg = generate(20000, seed=1)
    per_subject: dict[str, int] = {}
    for c in kg.courses.values():
        per_subject[c.subject] = per_subject.get(c.subject, 0) + 1
    assert max(per_subject.values()) <= 30
    assert max(c.budget for c in kg.courses.values()) <= 200


def test_validate_under_10_seconds_on_20000_topics(tmp_path):
    write_graph(generate(20000, seed=1, root=tmp_path))
    start = time.perf_counter()
    run_checks(load_graph(tmp_path))
    assert time.perf_counter() - start < 10
