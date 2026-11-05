import shutil
from pathlib import Path

import pytest

from kg.graph import KnowledgeGraph
from kg.model import Course, Topic
from kg.store import GraphLoadError, load_graph, write_course, write_graph

FIXTURE = Path(__file__).parent / "fixtures" / "sample"


# --- helpers (T4 moves the shared ones to conftest.py) ---


def snapshot(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*.yaml"))}


def read_any_course(root: Path) -> str:
    return (root / "math" / "alg1.yaml").read_text(encoding="utf-8")


def stub(topic_id: str, name: str = "X") -> Topic:
    return Topic(id=topic_id, name=name, status="stub")


def write_topic_named(root: Path, name: str) -> None:
    write_course(root, "math.a", [stub("math.a.x", name)])


def only_topic(kg: KnowledgeGraph) -> Topic:
    (topic,) = kg.topics.values()
    return topic


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


# --- tests ---


def test_round_trip_is_byte_identical(sample_copy):
    before = snapshot(sample_copy)
    write_graph(load_graph(sample_copy))
    assert snapshot(sample_copy) == before


def test_fixture_loads_with_expected_shape(sample_copy):
    kg = load_graph(sample_copy)
    assert len(kg.topics) == 15
    assert list(kg.courses) == ["math.arith", "math.alg1", "physics.mech"]
    assert [t.is_stub for t in kg.topics.values()].count(True) == 1
    assert sum(1 for t in kg.topics.values() if t.encompassed) == 1
    assert kg.duplicate_ids == []
    assert kg.history == []
    # insertion order follows courses.yaml, then unlisted course files
    ids = list(kg.topics)
    assert ids[0] == "math.arith.add-whole-numbers"
    assert ids[-1] == "math.trig.resolve-vector-components"


@pytest.mark.parametrize("text", ["No", "1.5", "Force: a review", "null", "</script>&<b>'\"π"])
def test_sensitive_strings_round_trip(tmp_graph, text):
    write_topic_named(tmp_graph, text)
    assert only_topic(load_graph(tmp_graph)).name == text


def test_all_bad_files_are_reported_with_names(tmp_graph):
    (tmp_graph / "math/a.yaml").write_text("course: [unclosed", encoding="utf-8")
    (tmp_graph / "math/b.yaml").write_text(
        "course: math.b\ntopics:\n- {id: math.b.x, name: X, status: stub, bogus: 1}\n",
        encoding="utf-8",
    )
    with pytest.raises(GraphLoadError) as e:
        load_graph(tmp_graph)
    assert {p.name for p, _ in e.value.problems} == {"a.yaml", "b.yaml"}


def test_unknown_level_is_a_load_error_naming_the_file(tmp_graph):
    (tmp_graph / "math/a.yaml").write_text(
        "course: math.a\ntopics:\n- {id: math.a.x, name: X, subject: math, course: math.a,"
        " level: g99, status: draft}\n",
        encoding="utf-8",
    )
    (tmp_graph / "courses.yaml").write_text(
        "courses:\n- {id: math.a, subject: math, levels: [g4, grade5], budget: 3}\n",
        encoding="utf-8",
    )
    with pytest.raises(GraphLoadError) as e:
        load_graph(tmp_graph)
    problems = {p.name: msg for p, msg in e.value.problems}
    assert "g99" in problems["a.yaml"]
    assert "grade5" in problems["courses.yaml"]


def test_missing_root_is_a_load_error(tmp_path):
    with pytest.raises(GraphLoadError):
        load_graph(tmp_path / "nope")


def test_duplicate_ids_are_recorded_not_lost(tmp_graph_with_duplicate):
    assert load_graph(tmp_graph_with_duplicate).duplicate_ids == ["math.a.x"]


def test_key_prerequisites_written_in_flow_style(sample_copy):
    assert "key_prerequisites: [" in read_any_course(sample_copy)


def test_write_graph_touches_only_changed_files(sample_copy):
    kg = load_graph(sample_copy)
    mtimes = {p: p.stat().st_mtime_ns for p in sample_copy.rglob("*.yaml")}
    kg.topics["math.alg1.combine-like-terms"].name = "Combining like terms, renamed"
    write_graph(kg)
    changed = {p.name for p, m in mtimes.items() if p.stat().st_mtime_ns != m}
    assert changed == {"alg1.yaml"}


def test_history_written_only_when_present(tmp_graph):
    kg = KnowledgeGraph(root=tmp_graph)
    kg.courses["math.a"] = Course(id="math.a", subject="math", levels=("g4", "g5"), budget=3)
    kg.topics["math.a.x"] = stub("math.a.x")
    write_graph(kg)
    assert not (tmp_graph / "id-history.yaml").exists()

    from kg.model import HistoryEntry

    kg.history.append(HistoryEntry(op="rename", source="math.a.old", targets=["math.a.x"]))
    write_graph(kg)
    assert load_graph(tmp_graph).history == kg.history


def test_view_course_round_trips(tmp_graph):
    kg = KnowledgeGraph(root=tmp_graph)
    kg.courses["math.v"] = Course(
        id="math.v", subject="math", levels=("g4", "g5"), budget=0, view_topics=[]
    )
    write_graph(kg)
    assert load_graph(tmp_graph).courses["math.v"].is_view


def test_files_are_lf_utf8(sample_copy):
    write_topic_named(sample_copy, "π")
    data = (sample_copy / "math" / "a.yaml").read_bytes()
    assert b"\r" not in data
    assert "π".encode("utf-8") in data
