from collections import defaultdict
from statistics import mean, quantiles

from conftest import add, course, stub, topic
from kg.graph import KnowledgeGraph
from kg.map.layout import (
    LINE_SPACING,
    STAGE_SPACING,
    flow_positions,
    level_floors,
    topic_depths,
    topic_stages,
)
from kg.synthetic import generate


def _graph(*courses_, topics=()):
    kg = KnowledgeGraph()
    for c in courses_:
        kg.courses[c.id] = c
    add(kg, *topics)
    return kg


def _chain(prefix, n, level="gk"):
    """prefix.t0 ... prefix.t{n-1}, each requiring the one before."""
    return [
        topic(f"{prefix}.t{i}", [f"{prefix}.t{i - 1}"] if i else None, level=level) for i in range(n)
    ]


def _by_stage(kg):
    stages = topic_stages(kg)
    pos = flow_positions(kg)
    grouped = defaultdict(list)
    for tid, s in stages.items():
        grouped[s].append(tid)
    return {s: sorted(ids, key=lambda t: pos[t][1]) for s, ids in grouped.items()}


def _crossings(kg, pos):
    edges = [(p.topic, t.id) for t in kg.topics.values() for p in t.prerequisites]
    n = 0
    for i, (a, b) in enumerate(edges):
        for c, d in edges[i + 1 :]:
            if pos[a][0] == pos[c][0] and pos[b][0] == pos[d][0]:
                if (pos[a][1] - pos[c][1]) * (pos[b][1] - pos[d][1]) < 0:
                    n += 1
    return n


def test_every_topic_is_right_of_its_prerequisites():
    kg = generate(500)
    pos = flow_positions(kg)
    for t in kg.topics.values():
        for p in t.prerequisites:
            if p.topic in kg.topics:
                assert pos[p.topic][0] < pos[t.id][0]


def test_depth_follows_the_deepest_prerequisite():
    kg = _graph(
        course("math.x", 3, levels=("gk", "g1")),
        topics=[
            topic("math.x.a", level="gk"),
            topic("math.x.b", ["math.x.a"], level="gk"),
            topic("math.x.c", ["math.x.b", "math.x.a"], level="gk"),
        ],
    )
    d = topic_depths(kg)
    assert (d["math.x.a"], d["math.x.b"], d["math.x.c"]) == (0, 1, 2)


def test_first_level_floor_is_zero():
    kg = _graph(course("math.x", 3, levels=("gk", "g1")), topics=_chain("math.x", 3))
    assert level_floors(kg, topic_depths(kg)) == {"gk": 0}


def _quartile_graph():
    gk = _chain("math.x", 7)
    g3 = [topic(f"math.y.u{i}", [f"math.x.t{i + 3}"], level="g3") for i in range(4)]
    return _graph(
        course("math.x", 7, levels=("gk", "gk")), course("math.y", 4, ["math.x"]), topics=gk + g3
    )


def test_floor_uses_the_lower_quartile():
    kg = _quartile_graph()
    depths = topic_depths(kg)
    d = [depths[f"math.y.u{i}"] for i in range(4)]
    assert d == [4, 5, 6, 7]
    assert quantiles(d, n=4, method="inclusive")[0] == 4.75
    assert level_floors(kg, depths)["g3"] == 4


def _shallow_graph():
    return _graph(
        course("math.x", 1, levels=("gk", "gk")),
        course("math.y", 1, ["math.x"]),
        topics=[topic("math.x.a", level="gk"), topic("math.y.b", level="g3")],
    )


def test_floors_always_increase():
    kg = _shallow_graph()
    assert level_floors(kg, topic_depths(kg)) == {"gk": 0, "g3": 1}


def test_shallow_high_level_topic_waits_for_its_floor():
    kg = _shallow_graph()
    floors = level_floors(kg, topic_depths(kg))
    assert topic_depths(kg)["math.y.b"] == 0
    assert topic_stages(kg)["math.y.b"] == floors["g3"]


def test_inverted_level_prerequisite_stays_ordered():
    kg = _graph(
        course("math.x", 1, levels=("g5", "g5")),
        course("math.y", 1, ["math.x"]),
        topics=[topic("math.x.a", level="g5"), topic("math.y.b", ["math.x.a"], level="g2")],
    )
    s = topic_stages(kg)
    assert s["math.y.b"] > s["math.x.a"]


def test_stub_has_stage_zero_and_dependent_follows():
    kg = _graph(
        course("math.x", 1, levels=("g5", "g5")),
        topics=[stub("math.later.s"), topic("math.x.a", ["math.later.s"], level="g5")],
    )
    s = topic_stages(kg)
    assert s["math.later.s"] == 0
    assert s["math.x.a"] >= 1


def test_unknown_course_and_subject_still_get_positions():
    kg = _graph(
        course("math.x", 1, levels=("g1", "g1")),
        topics=[
            topic("math.x.a", level="g1"),
            topic("bio.x.b", level="g1"),
            topic("zzz.y.c", level="g1"),
        ],
    )
    pos = flow_positions(kg)
    assert set(pos) == set(kg.topics)
    assert [t for t in _by_stage(kg)[0]] == ["math.x.a", "bio.x.b", "zzz.y.c"]


def test_stage_groups_by_subject_then_course():
    kg = _graph(
        course("math.a", 2, levels=("g1", "g1")),
        course("math.b", 2, levels=("g1", "g1")),
        course("physics.p", 1, levels=("g1", "g1")),
        topics=[
            topic("physics.p.z", level="g1"),
            topic("math.b.a", level="g1"),
            topic("math.a.z", level="g1"),
            topic("math.a.b", level="g1"),
        ],
    )
    assert _by_stage(kg)[0] == ["math.a.b", "math.a.z", "math.b.a", "physics.p.z"]


def test_courses_stay_contiguous_within_a_stage():
    kg = generate(500)
    for ids in _by_stage(kg).values():
        courses = [kg.topics[t].course_id for t in ids]
        collapsed = [c for i, c in enumerate(courses) if i == 0 or c != courses[i - 1]]
        assert len(collapsed) == len(set(collapsed))


def test_each_stage_is_centred():
    kg = generate(500)
    pos = flow_positions(kg)
    for ids in _by_stage(kg).values():
        ys = [pos[t][1] for t in ids]
        assert abs(mean(ys)) < 1e-9
        assert all(abs(b - a - LINE_SPACING) < 1e-9 for a, b in zip(ys, ys[1:]))


def test_sweeps_reduce_crossings():
    kg = _graph(
        course("math.x", 4, levels=("g1", "g1")),
        topics=[
            topic("math.x.a1", level="g1"),
            topic("math.x.b1", level="g1"),
            topic("math.x.a2", ["math.x.b1"], level="g1"),
            topic("math.x.b2", ["math.x.a1"], level="g1"),
        ],
    )
    id_order = {}
    stages = topic_stages(kg)
    by = defaultdict(list)
    for tid in sorted(kg.topics):
        by[stages[tid]].append(tid)
    for s, ids in by.items():
        for i, tid in enumerate(ids):
            id_order[tid] = (s * STAGE_SPACING, i - (len(ids) - 1) / 2)
    assert _crossings(kg, id_order) == 1
    assert _crossings(kg, flow_positions(kg)) == 0


def test_positions_are_repeatable():
    assert flow_positions(generate(500)) == flow_positions(generate(500))


def test_no_two_topics_share_a_position():
    pos = flow_positions(generate(500))
    assert len(set(pos.values())) == len(pos)


def test_empty_graph_gives_no_positions():
    assert flow_positions(KnowledgeGraph()) == {}


def test_view_courses_add_no_positions():
    kg = _graph(
        course("math.x", 2, levels=("g1", "g1")),
        topics=[topic("math.x.a", level="g1"), topic("math.x.b", level="g1")],
    )
    view = course("math.view", 0, levels=("g1", "g1"))
    view.view_topics = ["math.x.a", "math.x.b"]
    kg.courses["math.view"] = view
    pos = flow_positions(kg)
    assert len(pos) == len(kg.topics) == 2
