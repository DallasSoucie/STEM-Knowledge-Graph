import pytest
from conftest import edge

from kg.graph import GraphIndex, KnowledgeGraph, build_digraph, lineage, shortest_path
from kg.limits import course_closure, is_near_limits
from kg.model import Course, KnowledgePoint, Topic


def chain_graph(ids: list[str], extra: dict[str, list[str]] | None = None) -> KnowledgeGraph:
    """ids[i] requires ids[i-1]; `extra` adds more prerequisites by id."""
    kg = KnowledgeGraph()
    for i, tid in enumerate(ids):
        prereqs = [ids[i - 1]] if i else []
        prereqs += (extra or {}).get(tid, [])
        kg.topics[tid] = Topic(
            id=tid, name=tid, status="stub", prerequisites=[edge(p) for p in prereqs]
        )
    return kg


def test_is_ancestor_multi_hop():
    kg = chain_graph(["a", "b", "c", "d"])
    idx = GraphIndex(kg)
    assert idx.is_ancestor("a", "d")
    assert not idx.is_ancestor("d", "a")
    assert not idx.is_ancestor("a", "a")
    assert idx.ancestors("d") == {"a", "b", "c"}
    assert idx.descendants("a") == {"b", "c", "d"}
    assert idx.cycles() == []


def test_dangling_prerequisite_is_skipped():
    kg = chain_graph(["a", "b"], {"b": ["ghost"]})
    g = build_digraph(kg)
    assert set(g.edges) == {("a", "b")}
    assert GraphIndex(kg).ancestors("b") == {"a"}
    assert not GraphIndex(kg).is_ancestor("ghost", "b")


def test_cycle_is_reported_and_ancestors_do_not_hang():
    kg = chain_graph(["a", "b", "c", "d"], {"a": ["c"]})  # a<-c, c<-b, b<-a: cycle a,b,c
    idx = GraphIndex(kg)
    (cycle,) = idx.cycles()
    assert set(cycle) == {"a", "b", "c"}
    assert idx.ancestors("d") == {"a", "b", "c"}
    assert idx.ancestors("a") == {"b", "c"}
    assert idx.is_ancestor("b", "a") and idx.is_ancestor("a", "b")
    assert idx.descendants("a") == {"b", "c", "d"}


def test_lineage_respects_max_steps():
    kg = chain_graph(["a", "b", "c", "d"])
    assert lineage(kg, "d", "prerequisites", 1) == {"c"}
    assert lineage(kg, "d", "prerequisites", None) == {"a", "b", "c"}
    assert lineage(kg, "b", "dependents", 1) == {"c"}
    assert lineage(kg, "b", "both", 1) == {"a", "c"}
    assert lineage(kg, "nope", "both", None) == set()


def test_lineage_both_is_ancestors_plus_dependents_only():
    # a -> b -> c -> d, and x also requires a: x is an ancestor's other dependent, not c's relative
    kg = chain_graph(["a", "b", "c", "d"])
    kg.topics["x"] = Topic(id="x", name="x", status="stub", prerequisites=[edge("a")])
    assert lineage(kg, "c", "both", None) == {"a", "b", "d"}
    assert "x" not in lineage(kg, "c", "both", None)
    # maxSteps applies per direction
    assert lineage(kg, "b", "both", 1) == {"a", "c"}
    assert lineage(kg, "c", "both", 2) == {"a", "b", "d"}
    assert lineage(kg, "a", "both", 1) == {"b", "x"}


def test_shortest_path():
    kg = chain_graph(["a", "b", "c", "d"], {"d": ["a"]})
    assert shortest_path(kg, "a", "d") == ["a", "d"]
    assert shortest_path(kg, "d", "a") is None
    assert shortest_path(kg, "a", "zzz") is None


def kp(n: int, key_prereqs: int) -> KnowledgePoint:
    return KnowledgePoint(
        id=f"kp{n}", can_do="x", key_prerequisites=[f"p{i}" for i in range(key_prereqs)]
    )


def topic(prereqs: int = 1, kps: list[int] | None = None, status: str = "draft") -> Topic:
    kps = [1, 1, 1] if kps is None else kps
    return Topic(
        id="math.a.t",
        name="T",
        status=status,
        subject="math",
        course="math.a",
        level="g8",
        prerequisites=[edge(f"math.a.p{i}") for i in range(prereqs)],
        knowledge_points=[kp(n, k) for n, k in enumerate(kps)],
    )


@pytest.mark.parametrize(
    "t,expected",
    [
        (topic(), False),
        (topic(prereqs=3, kps=[3, 3, 2]), False),
        (topic(prereqs=4), True),
        (topic(kps=[4, 1, 1]), True),
        (topic(kps=[1, 1]), True),
        (topic(kps=[1, 1, 1, 1, 1]), True),
        (topic(kps=[3, 3, 3]), True),
        (topic(prereqs=5, status="stub", kps=[]), False),
    ],
)
def test_near_limits(t, expected):
    assert is_near_limits(t) is expected


def test_course_closure_survives_follows_cycle():
    kg = KnowledgeGraph()
    for cid, follows in [("math.a", ["math.b"]), ("math.b", ["math.c", "math.gone"]), ("math.c", ["math.a"])]:
        kg.courses[cid] = Course(id=cid, subject="math", levels=("g1", "g2"), budget=1, follows=follows)
    assert course_closure(kg, "math.a") == {"math.a", "math.b", "math.c"}
    assert course_closure(kg, "math.unknown") == {"math.unknown"}
