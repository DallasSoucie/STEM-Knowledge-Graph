from pathlib import Path

import pytest

from kg.graph import KnowledgeGraph
from kg.model import Course, Topic
from conftest import stub
from kg.store import GraphLoadError, load_graph, write_course, write_graph


def snapshot(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*.yaml"))}


def read_any_course(root: Path) -> str:
    return (root / "math" / "alg1.yaml").read_text(encoding="utf-8")


def write_topic_named(root: Path, name: str) -> None:
    write_course(root, "math.a", [stub("math.a.x", name)])


def only_topic(kg: KnowledgeGraph) -> Topic:
    (topic,) = kg.topics.values()
    return topic


# --- tests ---


def test_round_trip_is_byte_identical(sample_copy):
    before = snapshot(sample_copy)
    write_graph(load_graph(sample_copy))
    assert snapshot(sample_copy) == before


def test_fixture_loads_with_expected_shape(sample_copy):
    kg = load_graph(sample_copy)
    assert len(kg.topics) == 15
    assert list(kg.courses) == ["math.arith", "math.alg1", "physics.mech", "math.trig"]
    assert [t.is_stub for t in kg.topics.values()].count(True) == 1
    assert sum(1 for t in kg.topics.values() if t.encompassed) == 5
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


def test_topic_in_a_file_of_another_course_is_a_load_error(tmp_graph):
    (tmp_graph / "math/a.yaml").write_text(
        "course: math.a\ntopics:\n- {id: math.a.x, name: X, status: stub}\n"
        "- {id: math.b.y, name: Y, status: stub}\n",
        encoding="utf-8",
    )
    with pytest.raises(GraphLoadError) as e:
        load_graph(tmp_graph)
    ((path, msg),) = e.value.problems
    assert path.name == "a.yaml" and "math.b.y" in msg and "math.a.x" not in msg


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


def test_parse_cache_follows_file_edits(sample_copy):
    first = load_graph(sample_copy)  # primes the cache
    path = next((sample_copy / "math").glob("*.yaml"))
    tid = next(t for t in first.topics.values() if t.course_id.endswith(path.stem)).id
    path.write_bytes(path.read_bytes().replace(f"name: {first.topics[tid].name}".encode(), b"name: Edited", 1))
    assert load_graph(sample_copy).topics[tid].name == "Edited"


def test_misnamed_course_file_is_a_load_problem(tmp_path):
    write_course(tmp_path, "math.a", [stub("math.a.x")])
    (tmp_path / "math" / "a.yaml").rename(tmp_path / "math" / "wrong.yaml")
    with pytest.raises(GraphLoadError) as exc:
        load_graph(tmp_path)
    (path, message), = exc.value.problems
    assert path.name == "wrong.yaml" and "math/a.yaml" in message


def test_two_files_declaring_one_course_is_a_load_problem(tmp_path):
    write_course(tmp_path, "math.a", [stub("math.a.x")])
    (tmp_path / "math" / "a2.yaml").write_text(
        "course: math.a\ntopics:\n- {id: math.a.y, name: Y, status: stub}\n", encoding="utf-8"
    )
    with pytest.raises(GraphLoadError) as exc:
        load_graph(tmp_path)
    assert [p.name for p, _ in exc.value.problems] == ["a2.yaml"]


@pytest.mark.parametrize("bad", ["../evil.x", "math.a/../../x", "math", "Math.A", "a.b.c", ""])
def test_write_course_refuses_ids_that_could_leave_the_root(tmp_path, bad):
    root = tmp_path / "graph"
    root.mkdir()
    with pytest.raises(ValueError):
        write_course(root, bad, [])
    assert not [p for p in tmp_path.rglob("*.yaml")]


def test_repeated_course_in_manifest_is_recorded(tmp_path):
    (tmp_path / "courses.yaml").write_text(
        "courses:\n"
        "- {id: math.a, subject: math, levels: [g4, g5], budget: 1}\n"
        "- {id: math.a, subject: math, levels: [g4, g5], budget: 2}\n",
        encoding="utf-8",
    )
    kg = load_graph(tmp_path)
    assert kg.duplicate_courses == ["math.a"]
