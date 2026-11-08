import pytest
from conftest import add, course, edge, stub, topic, valid_graph

from kg.checks import RULES, run_checks
from kg.graph import KnowledgeGraph
from kg.model import Course, KnowledgePoint

# --- builders that break exactly one rule of the valid graph ---


def _replace(kg: KnowledgeGraph, tid: str, **changes) -> None:
    kg.topics[tid] = kg.topics[tid].model_copy(update=changes)


def _stubs(kg: KnowledgeGraph, n: int) -> list[str]:
    ids = [f"math.a.s{i}" for i in range(n)]
    add(kg, *(stub(i) for i in ids))
    return ids


def duplicate_id():
    kg = valid_graph()
    kg.duplicate_ids = ["math.a.one"]
    return kg


def id_format():
    kg = valid_graph()
    add(kg, stub("math.a.Bad_Slug"), stub("math.a.x", prereqs=["math.a.Bad_Slug"]))
    return kg


def unknown_course():
    kg = valid_graph()
    add(kg, stub("math.zzz.x"))
    return kg


def dangling_reference():
    kg = valid_graph()
    _replace(kg, "math.a.two", prerequisites=[edge("math.a.one"), edge("math.a.ghost")])
    return kg


def cycle():
    kg = valid_graph()
    _replace(kg, "math.a.one", prerequisites=[edge("math.a.three")])
    return kg


def manifest_follows_cycle():
    kg = valid_graph()
    kg.courses["math.a"] = course("math.a", 3, ["math.b"])
    return kg


def kp_count():
    kg = valid_graph()
    _replace(kg, "math.a.two", knowledge_points=kg.topics["math.a.two"].knowledge_points[:1])
    return kg


def direct_prereq_limit():
    kg = valid_graph()
    ids = _stubs(kg, 4)
    _replace(kg, "math.b.four", prerequisites=[edge(i) for i in ["math.a.three", *ids]])
    return kg


def key_prereq_limit():
    kg = valid_graph()
    ids = _stubs(kg, 4)
    keys = ["math.a.three", *ids]
    _replace(kg, "math.b.four", prerequisites=[edge(k) for k in keys])
    kg.topics["math.b.four"].justification = "five on purpose"
    kg.topics["math.b.four"].knowledge_points[0].key_prerequisites = keys
    return kg


def weight_range():
    kg = valid_graph()
    _replace(kg, "math.a.two", prerequisites=[edge("math.a.one", 1.5)])
    return kg


def orphan():
    kg = valid_graph()
    add(kg, topic("math.a.alone", level="g4"))
    return kg


def stub_no_dependent():
    kg = valid_graph()
    add(kg, stub("math.a.unused"))
    return kg


def key_prereq_not_ancestor():
    kg = valid_graph()
    kg.topics["math.a.two"].knowledge_points[0].key_prerequisites = ["math.b.four"]
    return kg


def key_prereq_unweighted():
    kg = valid_graph()
    kg.topics["math.b.four"].knowledge_points[0].key_prerequisites = ["math.a.one"]
    return kg


def encompassed_not_ancestor():
    kg = valid_graph()
    _replace(kg, "math.a.two", encompassed=[edge("math.b.four")])
    return kg


def course_gap():
    kg = valid_graph()
    kg.courses["math.c"] = course("math.c", 1)
    add(kg, topic("math.c.x", ["math.a.one"], keys=["math.a.one"]))
    return kg


def learner_walk():
    kg = valid_graph()
    one = kg.topics.pop("math.a.one")
    kg.topics["math.a.one"] = one  # now listed after two and three
    return kg


def redundant_edge():
    kg = valid_graph()
    _replace(kg, "math.a.three", prerequisites=[edge("math.a.two"), edge("math.a.one")])
    return kg


def prereq_above_level():
    kg = valid_graph()
    _replace(kg, "math.a.one", level="g9")
    return kg


def congested_topic():
    kg = valid_graph()
    (s,) = _stubs(kg, 1)
    _replace(kg, "math.a.three", prerequisites=[edge("math.a.two"), edge(s)])
    for kp in kg.topics["math.a.three"].knowledge_points:
        kp.key_prerequisites = ["math.a.two", "math.a.one", s]
    return kg


def uncited_prerequisite():
    kg = valid_graph()
    (s,) = _stubs(kg, 1)
    t = kg.topics["math.a.three"]
    _replace(kg, "math.a.three", prerequisites=[*t.prerequisites, edge(s)])
    return kg


def no_prereq_above_gk():
    kg = valid_graph()
    _replace(kg, "math.a.one", level="g4")
    return kg


def weight_clustering():
    kg = valid_graph()
    prev = "math.a.three"
    for i in range(20):
        add(kg, stub(f"math.a.c{i}", prereqs=[prev]))
        prev = f"math.a.c{i}"
    add(kg, topic("math.b.end", [prev], keys=[prev]))
    return kg


def level_outside_course():
    kg = valid_graph()
    _replace(kg, "math.b.four", level="g9")  # math.b spans g4 to g6
    return kg


def budget_variance():
    kg = valid_graph()
    kg.courses["math.a"] = course("math.a", 10)
    return kg


CASES = [
    ("duplicate-id", duplicate_id),
    ("id-format", id_format),
    ("unknown-course", unknown_course),
    ("dangling-reference", dangling_reference),
    ("cycle", cycle),
    ("manifest-follows-cycle", manifest_follows_cycle),
    ("kp-count", kp_count),
    ("direct-prereq-limit", direct_prereq_limit),
    ("key-prereq-limit", key_prereq_limit),
    ("weight-range", weight_range),
    ("orphan", orphan),
    ("stub-no-dependent", stub_no_dependent),
    ("key-prereq-not-ancestor", key_prereq_not_ancestor),
    ("key-prereq-unweighted", key_prereq_unweighted),
    ("encompassed-not-ancestor", encompassed_not_ancestor),
    ("course-gap", course_gap),
    ("learner-walk", learner_walk),
    ("redundant-edge", redundant_edge),
    ("prereq-above-level", prereq_above_level),
    ("congested-topic", congested_topic),
    ("uncited-prerequisite", uncited_prerequisite),
    ("no-prereq-above-gk", no_prereq_above_gk),
    ("weight-clustering", weight_clustering),
    ("budget-variance", budget_variance),
    ("level-outside-course", level_outside_course),
]


def rules_fired(kg: KnowledgeGraph) -> set[str]:
    return {i.rule for i in run_checks(kg)}


@pytest.mark.parametrize("rule_name,build", CASES)
def test_rule_fires_on_its_broken_graph(rule_name, build):
    assert rule_name in rules_fired(build())


def test_every_registered_rule_has_a_case():
    assert {name for name, _ in CASES} == set(RULES)


def test_valid_graph_has_no_issues_at_all():
    assert run_checks(valid_graph()) == []


def test_clean_graph_has_no_errors(sample_graph):
    assert [i for i in run_checks(sample_graph) if i.severity == "error"] == []


def test_empty_graph_is_clean(empty_graph):
    assert run_checks(empty_graph) == []


def test_stub_is_exempt_from_kp_count(graph_with_used_stub):
    assert "kp-count" not in {i.rule for i in run_checks(graph_with_used_stub)}


def test_severities_match_the_spec():
    warnings = {
        "redundant-edge",
        "prereq-above-level",
        "congested-topic",
        "uncited-prerequisite",
        "no-prereq-above-gk",
        "weight-clustering",
        "budget-variance",
    }
    assert {n for n, r in RULES.items() if r.severity == "warning"} == warnings
    assert {i.severity for i in run_checks(redundant_edge()) if i.rule == "redundant-edge"} == {
        "warning"
    }


def test_issue_carries_topic_and_file_from_the_id():
    (found,) = [i for i in run_checks(weight_range()) if i.rule == "weight-range"]
    assert found.topic == "math.a.two"
    assert found.file == "math/a.yaml"
    assert found.severity == "error"


def test_manifest_issues_name_the_manifest_file():
    (found,) = [i for i in run_checks(manifest_follows_cycle()) if i.rule == "manifest-follows-cycle"]
    assert found.file == "courses.yaml" and found.topic is None


def test_ancestor_rules_skip_when_prerequisites_cycle():
    fired = rules_fired(cycle())
    assert "cycle" in fired
    assert not fired & {"key-prereq-not-ancestor", "encompassed-not-ancestor", "redundant-edge"}


@pytest.mark.parametrize(
    "n_prereqs,justification,fires",
    [
        (4, None, False),
        (5, None, True),
        (5, "bridges five areas", False),
        (6, "bridges six areas", True),
    ],
)
def test_direct_prereq_limit_boundaries(n_prereqs, justification, fires):
    kg = valid_graph()
    ids = _stubs(kg, n_prereqs - 1)
    _replace(
        kg,
        "math.b.four",
        prerequisites=[edge(i) for i in ["math.a.three", *ids]],
        justification=justification,
    )
    assert ("direct-prereq-limit" in rules_fired(kg)) is fires


@pytest.mark.parametrize("n_keys,fires", [(4, False), (5, True)])
def test_key_prereq_limit_boundaries(n_keys, fires):
    kg = valid_graph()
    ids = _stubs(kg, n_keys - 1)
    keys = ["math.a.three", *ids]
    _replace(kg, "math.b.four", prerequisites=[edge(k) for k in keys], justification="wide")
    kg.topics["math.b.four"].knowledge_points[0].key_prerequisites = keys
    assert ("key-prereq-limit" in rules_fired(kg)) is fires


def test_dangling_reference_covers_every_reference_kind():
    kg = valid_graph()
    _replace(kg, "math.a.two", encompassed=[edge("math.a.g1")])
    kg.topics["math.a.two"].knowledge_points[0].key_prerequisites = ["math.a.g2"]
    kg.courses["math.b"] = course("math.b", 1, ["math.g3"])
    kg.courses["math.v"] = Course(
        id="math.v", subject="math", levels=("g4", "g5"), budget=1, view_topics=["math.a.g4"]
    )
    messages = " ".join(i.message for i in run_checks(kg) if i.rule == "dangling-reference")
    for ghost in ("math.a.g1", "math.a.g2", "math.g3", "math.a.g4"):
        assert ghost in messages


def test_id_format_rejects_mismatched_subject_and_course_fields():
    kg = valid_graph()
    _replace(kg, "math.a.two", subject="physics")
    assert "id-format" in rules_fired(kg)
    kg = valid_graph()
    _replace(kg, "math.a.two", course="math.b")
    assert "id-format" in rules_fired(kg)


def test_unknown_course_does_not_cascade_into_gap_and_walk():
    fired = rules_fired(unknown_course())
    assert "unknown-course" in fired and not fired & {"course-gap", "learner-walk"}


def test_course_gap_is_transitive_through_follows():
    kg = valid_graph()
    kg.courses["math.c"] = course("math.c", 1, ["math.b"])  # b follows a
    add(kg, topic("math.c.x", ["math.a.three"], keys=["math.a.three"]))
    assert not rules_fired(kg) & {"course-gap", "learner-walk"}


def test_view_course_gap_and_walk():
    kg = valid_graph()
    kg.courses["math.v"] = Course(
        id="math.v",
        subject="math",
        levels=("g4", "g6"),
        budget=1,
        view_topics=["math.a.three", "math.a.two", "math.a.one"],
    )
    fired = rules_fired(kg)
    assert "course-gap" not in fired  # prerequisites sit inside the view
    # the view lists `three` before its prerequisite `two`, and math.v follows nothing
    assert "learner-walk" in fired
    kg.courses["math.v"] = kg.courses["math.v"].model_copy(
        update={"view_topics": ["math.a.one", "math.a.two", "math.a.three"]}
    )
    assert not rules_fired(kg) & {"course-gap", "learner-walk"}


def test_view_course_with_outside_prerequisite_is_a_gap():
    kg = valid_graph()
    kg.courses["math.v"] = Course(
        id="math.v", subject="math", levels=("g4", "g6"), budget=1, view_topics=["math.a.three"]
    )
    assert "course-gap" in rules_fired(kg)


def test_course_following_a_view_gets_the_views_topics():
    kg = valid_graph()
    kg.courses["math.v"] = Course(
        id="math.v",
        subject="math",
        levels=("g4", "g6"),
        budget=1,
        view_topics=["math.a.one", "math.a.two", "math.a.three"],
    )
    kg.courses["math.b"] = course("math.b", 1, ["math.v"])
    assert not rules_fired(kg) & {"course-gap", "learner-walk"}


@pytest.mark.parametrize(
    "budget,extra,fires",
    [(5, 0, True), (5, 3, False), (5, 4, True), (4, 2, True), (6, 3, False)],
)
def test_budget_variance_threshold_is_twenty_percent(budget, extra, fires):
    kg = valid_graph()  # math.a starts with 3 topics: actual is 3 + extra
    kg.courses["math.a"] = course("math.a", budget)
    for i in range(extra):
        add(kg, topic(f"math.a.x{i}", ["math.a.one"], keys=["math.a.one"]))
    assert ("budget-variance" in rules_fired(kg)) is fires


def test_weight_clustering_needs_twenty_weights():
    kg = weight_clustering()
    assert "weight-clustering" in rules_fired(kg)
    for i in range(16, 20):  # leaves 19 weights in math.a
        del kg.topics[f"math.a.c{i}"]
    del kg.topics["math.b.end"]
    assert "weight-clustering" not in rules_fired(kg)


def _clustered(counts: list[int]):
    """math.a holds one weight per entry, `counts[k]` of them on the k-th distinct value."""
    values = [round(0.05 + 0.04 * k, 2) for k in range(len(counts))]
    kg = KnowledgeGraph()
    kg.courses["math.a"] = course("math.a", 1)
    weights = [v for v, n in zip(values, counts) for _ in range(n)]
    prev = "math.a.c0"
    add(kg, stub(prev))
    for i, w in enumerate(weights, start=1):
        tid = f"math.a.c{i}"
        add(kg, stub(tid))
        kg.topics[tid].prerequisites.append(edge(prev, w))
        prev = tid
    return kg


@pytest.mark.parametrize(
    "counts,fires",
    [
        ([6, 5, 5, 1, 1, 1, 1], False),  # 16 of 20 is exactly 80%
        ([6, 6, 5, 1, 1, 1], True),  # 17 of 20
        ([8, 8, 3, 1], True),  # fires only if the third value is counted: top two are 16/20
        ([5, 5, 5, 1, 1, 1, 1, 1], False),  # 15 of 20
    ],
)
def test_weight_clustering_threshold(counts, fires):
    assert sum(counts) == 20
    assert ("weight-clustering" in rules_fired(_clustered(counts))) is fires


def test_kp_with_no_key_prerequisites_does_not_make_a_topic_congested():
    kg = valid_graph()
    (s0,) = _stubs(kg, 1)
    _replace(kg, "math.a.three", prerequisites=[edge("math.a.two"), edge(s0)])
    kps = kg.topics["math.a.three"].knowledge_points
    kps[0].key_prerequisites = ["math.a.two", "math.a.one", s0]
    kps[1].key_prerequisites = ["math.a.two", "math.a.one", s0]
    kps[2].key_prerequisites = []
    assert "congested-topic" not in rules_fired(kg)


def test_topic_filed_under_a_view_course_is_an_unknown_course():
    kg = valid_graph()
    kg.courses["math.v"] = Course(
        id="math.v", subject="math", levels=("g4", "g5"), budget=1, view_topics=["math.a.one"]
    )
    add(kg, stub("math.v.x"))
    (found,) = [i for i in run_checks(kg) if i.rule == "unknown-course"]
    assert found.topic == "math.v.x" and "view" in found.message


def test_validation_does_not_depend_on_the_map():
    import kg.checks.structure as s

    assert not hasattr(s, "lane_overflows")


def test_level_outside_course_ignores_stubs_and_in_range_topics():
    assert "level-outside-course" not in rules_fired(valid_graph())
    kg = level_outside_course()
    (found,) = [i for i in run_checks(kg) if i.rule == "level-outside-course"]
    assert found.severity == "error"
    assert found.topic == "math.b.four"


def _dup_messages(kg):
    return [i.message for i in run_checks(kg) if i.rule == "duplicate-id"]


def test_duplicate_entries_within_a_topic_are_flagged():
    kg = valid_graph()
    _replace(kg, "math.a.two", prerequisites=[edge("math.a.one"), edge("math.a.one", 0.2)])
    assert any("math.a.one" in m for m in _dup_messages(kg))

    kg = valid_graph()
    _replace(kg, "math.a.three", encompassed=[edge("math.a.one"), edge("math.a.one", 0.2)])
    assert any("math.a.one" in m for m in _dup_messages(kg))

    kg = valid_graph()
    kg.topics["math.a.two"].knowledge_points[1].id = "kp1"
    assert any("kp1" in m for m in _dup_messages(kg))


def test_repeated_course_in_manifest_is_flagged():
    kg = valid_graph()
    kg.duplicate_courses = ["math.a"]
    assert any("math.a" in m for m in _dup_messages(kg))
