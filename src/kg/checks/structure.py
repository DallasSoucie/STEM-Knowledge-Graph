"""Structural rules: IDs, references, cycles, limits, ancestry of key prerequisites."""

import re
from collections import Counter

from kg.checks.base import COURSES_FILE_NAME, is_acyclic, issue, rule
from kg.graph import GraphIndex, KnowledgeGraph
from kg.map.layout import LANE_CAPACITY, DEFAULT_LANE_CAPACITY, lane_overflows

_SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
_ID_RE = re.compile(rf"^{_SLUG}\.{_SLUG}\.{_SLUG}$")


@rule("duplicate-id", "error")
def duplicate_id(kg: KnowledgeGraph, index: GraphIndex):
    for tid in kg.duplicate_ids:
        yield issue("duplicate-id", f"ID {tid} is defined more than once", tid)
    for cid in kg.duplicate_courses:
        yield issue(
            "duplicate-id", f"course {cid} is listed more than once", file=COURSES_FILE_NAME
        )
    for tid, t in kg.topics.items():
        for kind, edges in (("prerequisite", t.prerequisites), ("encompassed topic", t.encompassed)):
            for target, n in Counter(e.topic for e in edges).items():
                if n > 1:
                    yield issue("duplicate-id", f"{kind} {target} is listed {n} times", tid)
        for kp_id, n in Counter(k.id for k in t.knowledge_points).items():
            if n > 1:
                yield issue("duplicate-id", f"knowledge point {kp_id} is defined {n} times", tid)


@rule("id-format", "error")
def id_format(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        if not _ID_RE.match(tid):
            yield issue("id-format", f"ID {tid!r} is not <subject>.<course>.<slug> in lowercase", tid)
            continue
        subject, short, _ = tid.split(".")
        if t.subject is not None and t.subject != subject:
            yield issue("id-format", f"subject {t.subject!r} does not match the ID", tid)
        if t.course is not None and t.course != f"{subject}.{short}":
            yield issue("id-format", f"course {t.course!r} does not match the ID", tid)


@rule("unknown-course", "error")
def unknown_course(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        course = kg.courses.get(t.course_id)
        if course is None:
            yield issue("unknown-course", f"course {t.course_id} is not in {COURSES_FILE_NAME}", tid)
        elif course.is_view:
            yield issue(
                "unknown-course",
                f"{t.course_id} is a view course; view courses own no topics",
                tid,
            )


@rule("dangling-reference", "error")
def dangling_reference(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        for kind, edges in (("prerequisite", t.prerequisites), ("encompassed topic", t.encompassed)):
            for e in edges:
                if e.topic not in kg.topics:
                    yield issue("dangling-reference", f"{kind} {e.topic} does not exist", tid)
        for kp in t.knowledge_points:
            for k in kp.key_prerequisites:
                if k not in kg.topics:
                    yield issue(
                        "dangling-reference", f"{kp.id}: key prerequisite {k} does not exist", tid
                    )
    for c in kg.courses.values():
        for f in c.follows:
            if f not in kg.courses:
                yield issue(
                    "dangling-reference",
                    f"course {c.id} follows unknown course {f}",
                    file=COURSES_FILE_NAME,
                )
        for v in c.view_topics or []:
            if v not in kg.topics:
                yield issue(
                    "dangling-reference",
                    f"view course {c.id} lists unknown topic {v}",
                    file=COURSES_FILE_NAME,
                )


@rule("cycle", "error")
def cycle(kg: KnowledgeGraph, index: GraphIndex):
    for members in index.cycles():
        yield issue("cycle", "prerequisite cycle: " + " -> ".join(members + members[:1]), members[0])


@rule("kp-count", "error")
def kp_count(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        n = len(t.knowledge_points)
        if not t.is_stub and not 2 <= n <= 5:
            yield issue("kp-count", f"{n} knowledge points; expected 2 to 5", tid)


@rule("direct-prereq-limit", "error")
def direct_prereq_limit(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        n = len(t.prerequisites)
        if n > 5:
            yield issue("direct-prereq-limit", f"{n} direct prerequisites; hard cap is 5", tid)
        elif n > 4 and not (t.justification and t.justification.strip()):
            yield issue(
                "direct-prereq-limit", f"{n} direct prerequisites need a justification", tid
            )


@rule("key-prereq-limit", "error")
def key_prereq_limit(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        for kp in t.knowledge_points:
            if len(kp.key_prerequisites) > 4:
                yield issue(
                    "key-prereq-limit", f"{kp.id}: {len(kp.key_prerequisites)} key prerequisites", tid
                )


@rule("weight-range", "error")
def weight_range(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        for e in (*t.prerequisites, *t.encompassed):
            if not 0.0 <= e.encompassing <= 1.0:
                yield issue(
                    "weight-range", f"weight {e.encompassing} on {e.topic} is outside 0-1", tid
                )


@rule("orphan", "error")
def orphan(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        if not t.is_stub and not t.prerequisites and index.graph.out_degree(tid) == 0:
            yield issue("orphan", "no prerequisites and no dependents", tid)


@rule("stub-no-dependent", "error")
def stub_no_dependent(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        if t.is_stub and index.graph.out_degree(tid) == 0:
            yield issue("stub-no-dependent", "stub has no dependent topic", tid)


@rule("key-prereq-not-ancestor", "error")
def key_prereq_not_ancestor(kg: KnowledgeGraph, index: GraphIndex):
    if not is_acyclic(index):
        return
    for tid, t in kg.topics.items():
        for kp in t.knowledge_points:
            for k in kp.key_prerequisites:
                if k in kg.topics and not index.is_ancestor(k, tid):
                    yield issue(
                        "key-prereq-not-ancestor", f"{kp.id}: {k} is not an ancestor of this topic", tid
                    )


@rule("key-prereq-unweighted", "error")
def key_prereq_unweighted(kg: KnowledgeGraph, index: GraphIndex):
    for tid, t in kg.topics.items():
        weighted = {e.topic for e in t.prerequisites} | {e.topic for e in t.encompassed}
        for kp in t.knowledge_points:
            for k in kp.key_prerequisites:
                if k in kg.topics and k not in weighted:
                    yield issue(
                        "key-prereq-unweighted",
                        f"{kp.id}: {k} is in neither prerequisites nor encompassed",
                        tid,
                    )


@rule("encompassed-not-ancestor", "error")
def encompassed_not_ancestor(kg: KnowledgeGraph, index: GraphIndex):
    if not is_acyclic(index):
        return
    for tid, t in kg.topics.items():
        for e in t.encompassed:
            if e.topic in kg.topics and not index.is_ancestor(e.topic, tid):
                yield issue(
                    "encompassed-not-ancestor", f"encompassed {e.topic} is not an ancestor", tid
                )


@rule("lane-overflow", "error")
def lane_overflow(kg: KnowledgeGraph, index: GraphIndex):
    """The map has a fixed number of lanes per subject row; more courses than fit cannot be laid out."""
    for cid, subject in lane_overflows(kg):
        yield issue(
            "lane-overflow",
            f"course {cid} needs more than {LANE_CAPACITY.get(subject, DEFAULT_LANE_CAPACITY)} "
            f"lanes in subject {subject}",
            file=COURSES_FILE_NAME,
        )
