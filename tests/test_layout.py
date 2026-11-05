from collections import defaultdict
from itertools import combinations
from pathlib import Path

import pytest

from conftest import add, course, stub, topic
from kg.graph import KnowledgeGraph
from kg.map.layout import LANE_CAPACITY, LINES_PER_LANE, column_bounds, compute_positions, lane_of, row_bounds
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
    rows = row_bounds(_two_course_graph())
    assert rows["math"][0] <= pos["math.a.t1"][1] < rows["math"][1]
    assert rows["physics"][0] <= pos["physics.p.u1"][1] < rows["physics"][1]
    assert rows["math"][1] <= rows["physics"][0]


def test_rows_ignore_what_the_other_subjects_hold():
    empty = row_bounds(_graph())
    assert row_bounds(_two_course_graph())["physics"] == empty["physics"]


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
    assert changed <= {"math.a.t1", "math.a.t2", "math.a.t3", "math.a.t4"}
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
    kg = _graph(*(course(f"math.c{i}", 1) for i in range(LANE_CAPACITY["math"] + 1)))
    with pytest.raises(ValueError, match="math"):
        lane_of(kg)


def test_real_manifest_and_synthetic_fit_lanes():
    root = Path(__file__).parent.parent / "graph"
    kg = load_graph(root)
    lanes = lane_of(kg)
    assert all(lane < LANE_CAPACITY[subject] for subject, lane in lanes.values())
    big = generate(20000, seed=1)
    assert all(lane < LANE_CAPACITY[subject] for subject, lane in lane_of(big).values())
    pos = compute_positions(big)
    assert len(pos) == len(big.topics)


def _width(kg, level):
    lo, hi = column_bounds(kg)[level]
    return hi - lo


def test_column_width_follows_budget_share_above_minimum():
    kg = _graph(course("math.a", 100, levels=("g4", "g4")))
    assert _width(kg, "g4") == 100 * 0.5


def test_smaller_course_does_not_change_column_width():
    big = _graph(course("math.a", 100, levels=("g4", "g4")))
    both = _graph(course("math.a", 100, levels=("g4", "g4")), course("physics.p", 10, levels=("g4", "g4")))
    assert _width(both, "g4") == _width(big, "g4")


def test_larger_share_widens_column():
    small = _graph(course("math.a", 60, levels=("g4", "g4")))
    large = _graph(course("math.a", 60, levels=("g4", "g4")), course("physics.p", 100, levels=("g4", "g4")))
    assert _width(large, "g4") > _width(small, "g4")


# ---- the real manifest, filled to budget ---------------------------------------------------------


def _filled_manifest(skew=False):
    """graph/courses.yaml with every course at its budget. Topics spread evenly over the course's
    levels, or with skew=True all sit at its lowest level (the worst case for one block)."""
    kg = load_graph(Path(__file__).parent.parent / "graph")
    kg.topics = {}
    for c in kg.courses.values():
        if c.is_view:
            continue
        lo, hi = (LEVELS.index(x) for x in c.levels)
        span = hi - lo + 1
        add(kg, *[
            topic(f"{c.id}.t{i}", level=LEVELS[lo if skew else lo + i * span // c.budget])
            for i in range(c.budget)
        ])
    return kg


def _bbox(points):
    xs, ys = zip(*points)
    return min(xs), max(xs), min(ys), max(ys)


def test_real_manifest_aspect_ratio():
    x0, x1, y0, y1 = _bbox(compute_positions(_filled_manifest()).values())
    assert 1.4 <= (x1 - x0) / (y1 - y0) <= 2.2


@pytest.mark.parametrize("skew", [False, True])
def test_course_blocks_do_not_overlap(skew):
    kg = _filled_manifest(skew)
    pos = compute_positions(kg)
    points = defaultdict(list)
    for tid, p in pos.items():
        points[kg.topics[tid].course].append(p)
    boxes = {cid: _bbox(pts) for cid, pts in points.items()}
    for a, b in combinations(boxes, 2):
        ax0, ax1, ay0, ay1 = boxes[a]
        bx0, bx1, by0, by1 = boxes[b]
        assert ax1 < bx0 or bx1 < ax0 or ay1 < by0 or by1 < ay0, (a, b)


@pytest.mark.parametrize("skew", [False, True])
def test_no_two_topics_share_a_position(skew):
    pos = compute_positions(_filled_manifest(skew))
    assert len(set(pos.values())) == len(pos)


def test_course_wraps_onto_multiple_lines():
    kg = _graph(course("math.a", 200, levels=("g4", "g4")))
    add(kg, *[topic(f"math.a.t{i}", level="g4") for i in range(200)])
    assert len({y for _, y in compute_positions(kg).values()}) > 1


def test_growing_a_course_within_budget_moves_only_its_topics():
    kg = _filled_manifest()
    grown = "math.g5"
    for tid in [t for t in kg.topics if t.startswith(grown + ".") and int(t.rsplit("t", 1)[1]) >= 80]:
        del kg.topics[tid]
    before = compute_positions(kg)
    add(kg, *[topic(f"{grown}.t{i}", level="g5") for i in range(80, 160)])
    after = compute_positions(kg)
    moved = {t for t in before if before[t] != after[t]}
    assert all(t.startswith(grown + ".") for t in moved)


def test_course_past_its_budget_stays_inside_its_lane_and_column():
    kg = _graph(course("math.a", 10, levels=("g4", "g4")))
    add(kg, *[topic(f"math.a.t{i}", level="g4") for i in range(500)])
    pos = compute_positions(kg)
    x0, x1 = column_bounds(kg)["g4"]
    assert len(set(pos.values())) == 500
    assert all(x0 <= x <= x1 for x, _ in pos.values())
    assert len({y for _, y in pos.values()}) == LINES_PER_LANE
