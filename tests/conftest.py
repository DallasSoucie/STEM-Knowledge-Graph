"""Shared builders and fixtures."""

import shutil
from pathlib import Path

import pytest

from kg.graph import KnowledgeGraph
from kg.model import Course, Edge, KnowledgePoint, Topic
from kg.store import load_graph, write_course

FIXTURE = Path(__file__).parent / "fixtures" / "sample"


def edge(target: str, weight: float = 0.5, confidence: str = "high") -> Edge:
    return Edge(topic=target, encompassing=weight, confidence=confidence)


def stub(topic_id: str, name: str = "X", prereqs: list[str] | None = None) -> Topic:
    return Topic(
        id=topic_id, name=name, status="stub", prerequisites=[edge(p) for p in prereqs or []]
    )


def topic(
    topic_id: str,
    prereqs: list[str] | None = None,
    *,
    keys: list[str] | None = None,
    encompassed: list[str] | None = None,
    level: str = "g5",
    n_kps: int = 3,
) -> Topic:
    """A draft topic whose every KP lists `keys` as key prerequisites."""
    subject, course, _ = topic_id.split(".")
    return Topic(
        id=topic_id,
        name=topic_id,
        status="draft",
        subject=subject,
        course=f"{subject}.{course}",
        level=level,
        prerequisites=[edge(p) for p in prereqs or []],
        encompassed=[edge(p, 0.3) for p in encompassed or []],
        knowledge_points=[
            KnowledgePoint(id=f"kp{i}", can_do=f"Do step {i}", key_prerequisites=list(keys or []))
            for i in range(1, n_kps + 1)
        ],
    )


def course(course_id: str, budget: int, follows: list[str] | None = None, levels=("g4", "g6")):
    return Course(
        id=course_id,
        subject=course_id.split(".")[0],
        levels=levels,
        budget=budget,
        follows=follows or [],
    )


def add(kg: KnowledgeGraph, *topics: Topic) -> None:
    for t in topics:
        kg.topics[t.id] = t


def valid_graph() -> KnowledgeGraph:
    """Small graph that passes every rule with no issues at all."""
    kg = KnowledgeGraph()
    kg.courses = {
        "math.a": course("math.a", 3),
        "math.b": course("math.b", 1, ["math.a"]),
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
        topic("math.b.four", ["math.a.three"], keys=["math.a.three"], level="g6"),
    )
    return kg


@pytest.fixture
def sample_graph():
    return load_graph(FIXTURE)


@pytest.fixture
def empty_graph():
    return KnowledgeGraph()


@pytest.fixture
def graph_with_used_stub():
    kg = valid_graph()
    add(kg, stub("math.a.later"))
    kg.topics["math.b.four"] = topic(
        "math.b.four", ["math.a.three", "math.a.later"], keys=["math.a.three"], level="g6"
    )
    return kg


@pytest.fixture
def sample_copy(tmp_path):
    dest = tmp_path / "graph"
    shutil.copytree(FIXTURE, dest)
    return dest


@pytest.fixture
def tmp_graph(tmp_path):
    (tmp_path / "math").mkdir()
    return tmp_path


@pytest.fixture
def tmp_graph_with_duplicate(tmp_graph):
    write_course(tmp_graph, "math.a", [stub("math.a.x")])
    # same id again, from a second file that claims the same course
    (tmp_graph / "math" / "a2.yaml").write_text(
        "course: math.a\ntopics:\n- {id: math.a.x, name: Again, status: stub}\n", encoding="utf-8"
    )
    return tmp_graph
