from pathlib import Path

import pytest

from conftest import add, course, stub, topic
from kg.graph import KnowledgeGraph
from kg.map.layout import ROW_LANES, column_bounds, compute_positions, lane_of
from kg.model import LEVELS
from kg.store import load_graph
from kg.synthetic import generate


def _graph(*courses_, topics=()):
    kg = KnowledgeGraph()
    for c in courses_:
        kg.courses[c.id] = c
    add(kg, *topics)
    return kg


def _two_course_graph():
    return _graph(
        course("math.a", 4, levels=("g4", "g6")),
        course("physics.p", 4, levels=("g5", "g7")),
        topics=[
            topic("math.a.t1", level="g4"),
            topic("math.a.t2", level="g5"),
            topic("math.a.t3", level="g5"),
            topic("math.a.t4", level="g6"),
            topic("physics.p.u1", level="g5"),
            topic("physics.p.u2", level="g7"),
        ],
    )


def test_positions_are_repeatable():
    assert compute_positions(_two_course_graph()) == compute_positions(_two_course_graph())


def test_lower_levels_are_left_of_higher():
    pos = compute_positions(_two_course_graph())
    assert pos["math.a.t1"][0] < pos["math.a.t2"][0] < pos["math.a.t4"][0]
    bounds = column_bounds(_two_course_graph())
    for lo, hi in zip(LEVELS, LEVELS[1:]):
        assert bounds[lo][1] <= bounds[hi][0]


def test_subjects_occupy_separate_rows():
    pos = compute_positions(_two_course_graph())
    assert pos["math.a.t1"][1] < ROW_LANES <= pos["physics.p.u1"][1] < 2 * ROW_LANES


def test_same_level_courses_get_separate_lanes():
    kg = _graph(course("math.a", 2), course("math.b", 2))
    lanes = lane_of(kg)
    assert lanes["math.a"][0] == lanes["math.b"][0] == "math"
    assert lanes["math.a"][1] != lanes["math.b"][1]


def test_nonoverlapping_courses_share_a_lane():
    kg = _graph(course("math.a", 2, levels=("g1", "g2")), course("math.b", 2, levels=("g3", "g4")))
    lanes = lane_of(kg)
    assert lanes["math.a"] == lanes["math.b"]


def test_view_courses_get_no_lane():
    kg = _graph(course("math.a", 2))
    view = course("math.v", 0)
    view.view_topics = ["math.a.x"]
    kg.courses[view.id] = view
    assert "math.v" not in lane_of(kg)


def test_adding_topic_moves_only_its_course():
    kg = _two_course_graph()
    before = compute_positions(kg)
    add(kg, topic("math.a.t5", level="g5"))
    after = compute_positions(kg)
    changed = {t for t in before if before[t] != after[t]}
    assert changed == {"math.a.t2", "math.a.t3"}
    assert "math.a.t5" in after


def test_adding_course_within_budget_max_leaves_other_rows_unmoved():
    kg = _two_course_graph()
    before = compute_positions(kg)
    kg.courses["math.b"] = course("math.b", 2, levels=("g5", "g6"))
    add(kg, topic("math.b.z", level="g5"))
    after = compute_positions(kg)
    for tid, p in before.items():
        assert after[tid] == p


def test_empty_graph_gives_no_positions():
    kg = KnowledgeGraph()
    assert compute_positions(kg) == {}
    assert lane_of(kg) == {}


def test_stub_without_level_gets_position():
    kg = _graph(course("math.a", 1, levels=("g4", "g6")), topics=[topic("math.a.t", level="g5")])
    add(kg, stub("math.a.later"))
    pos = compute_positions(kg)
    assert column_bounds(kg)["g4"][0] <= pos["math.a.later"][0] <= column_bounds(kg)["g4"][1]


def test_too_many_lanes_raises_clear_error():
    kg = _graph(*(course(f"math.c{i}", 1) for i in range(ROW_LANES + 1)))
    with pytest.raises(ValueError, match="math"):
        lane_of(kg)


def test_real_manifest_and_synthetic_fit_lanes():
    root = Path(__file__).parent.parent / "graph"
    kg = load_graph(root)
    lanes = lane_of(kg)
    assert all(lane < ROW_LANES for _, lane in lanes.values())
    big = generate(20000, seed=1)
    assert all(lane < ROW_LANES for _, lane in lane_of(big).values())
    pos = compute_positions(big)
    assert len(pos) == len(big.topics)
