"""Quality warnings."""

from collections import Counter

from kg.checks.base import COURSES_FILE_NAME, is_acyclic, issue, rule
from kg.graph import GraphIndex, KnowledgeGraph
from kg.model import level_rank


@rule("redundant-edge", "warning")
def redundant_edge(kg: KnowledgeGraph, index: GraphIndex):
    if not is_acyclic(index):
        return
    for tid, t in kg.topics.items():
        direct = [e.topic for e in t.prerequisites if e.topic in kg.topics]
        for p in dict.fromkeys(direct):
            via = next((q for q in direct if q != p and index.is_ancestor(p, q)), None)
            if via is not None:
                yield issue("redundant-edge", f"{p} is already implied through {via}", tid)


@rule("prereq-above-level", "warning")
def prereq_above_level(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        if t.level is None:
            continue
        for e in t.prerequisites:
            p = kg.topics.get(e.topic)
            if p is not None and p.level is not None and level_rank(p.level) > level_rank(t.level):
                yield issue(
                    "prereq-above-level",
                    f"prerequisite {e.topic} is level {p.level}, above {t.level}",
                    tid,
                )


@rule("level-outside-course", "warning")
def level_outside_course(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        course = kg.courses.get(t.course_id)
        if t.is_stub or t.level is None or course is None or course.is_view:
            continue
        lo, hi = sorted(level_rank(x) for x in course.levels)
        if not lo <= level_rank(t.level) <= hi:
            yield issue(
                "level-outside-course",
                f"level {t.level} is outside {course.id}'s range {course.levels[0]} to {course.levels[1]}",
                tid,
            )


@rule("congested-topic", "warning")
def congested_topic(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        kps = t.knowledge_points
        if not t.is_stub and kps and all(len(k.key_prerequisites) >= 3 for k in kps):
            yield issue("congested-topic", "every knowledge point has 3+ key prerequisites", tid)


@rule("no-prereq-above-gk", "warning")
def no_prereq_above_gk(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        if not t.is_stub and t.level not in (None, "gk") and not t.prerequisites:
            yield issue("no-prereq-above-gk", f"level {t.level} topic has no prerequisites", tid)


@rule("weight-clustering", "warning")
def weight_clustering(kg: KnowledgeGraph, index: GraphIndex):
    """Weights are the `encompassing` values on both prerequisite and encompassed edges."""
    by_course: dict[str, Counter] = {}
    for t in kg.topics.values():
        counts = by_course.setdefault(t.course_id, Counter())
        for e in (*t.prerequisites, *t.encompassed):
            counts[round(e.encompassing, 3)] += 1
    for course_id, counts in by_course.items():
        total = sum(counts.values())
        top = sum(n for _, n in counts.most_common(3))
        if total >= 20 and top / total > 0.8:
            subject, _, short = course_id.partition(".")
            yield issue(
                "weight-clustering",
                f"{top} of {total} weights in {course_id} sit on 3 values",
                file=f"{subject}/{short}.yaml",
            )


@rule("budget-variance", "warning")
def budget_variance(kg: KnowledgeGraph, index: GraphIndex):
    actual: Counter = Counter(t.course_id for t in kg.topics.values() if not t.is_stub)
    for c in kg.courses.values():
        n = actual.get(c.id, 0)
        if n and abs(n - c.budget) > 0.2 * c.budget:
            yield issue(
                "budget-variance",
                f"{n} topics against a budget of {c.budget}",
                file=COURSES_FILE_NAME,
            )
