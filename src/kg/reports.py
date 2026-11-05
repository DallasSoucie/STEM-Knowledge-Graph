"""Read-only reports: stats, review report, review queue, duplicate detection."""

import math
import re
from collections import Counter
from dataclasses import dataclass

import networkx as nx

from kg.graph import KnowledgeGraph, build_digraph
from kg.limits import is_near_limits
from kg.model import LEVELS, Topic

_CONFIDENCE = ("high", "medium", "low")
_WORD = re.compile(r"\w+")


def _subject(t: Topic) -> str:
    return t.subject or t.id.split(".")[0]


def _course(t: Topic) -> str:
    return t.course or t.course_id


def _scope(kg: KnowledgeGraph, course: str | None) -> dict[str, Topic]:
    if course is None:
        return kg.topics
    return {tid: t for tid, t in kg.topics.items() if _course(t) == course}


def _depths(kg: KnowledgeGraph) -> dict[str, int]:
    """Longest prerequisite chain below each topic. Cycles collapse to one level."""
    cond = nx.condensation(build_digraph(kg))
    depth: dict[int, int] = {}
    for c in nx.topological_sort(cond):
        depth[c] = max((depth[p] + 1 for p in cond.predecessors(c)), default=0)
    mapping = cond.graph["mapping"]
    return {tid: depth[mapping[tid]] for tid in kg.topics}


def stats(kg: KnowledgeGraph, course: str | None = None) -> dict:
    topics = _scope(kg, course)
    depths = _depths(kg) if topics else {}
    weights = [e.encompassing for t in topics.values() for e in t.prerequisites]
    confidence: dict[str, Counter] = {}
    for t in topics.values():
        c = confidence.setdefault(_course(t), Counter())
        for e in t.prerequisites:
            c[e.confidence] += 1
    courses = Counter(_course(t) for t in topics.values())
    levels = Counter(t.level or "none" for t in topics.values())
    return {
        "topics": len(topics),
        "by_subject": dict(sorted(Counter(_subject(t) for t in topics.values()).items())),
        "by_course": dict(sorted(courses.items())),
        "by_level": {lv: levels[lv] for lv in (*LEVELS, "none") if levels[lv]},
        "prerequisite_count": dict(
            sorted(Counter(len(t.prerequisites) for t in topics.values()).items())
        ),
        "kp_count": dict(
            sorted(Counter(len(t.knowledge_points) for t in topics.values()).items())
        ),
        "depth": dict(sorted(Counter(depths[tid] for tid in topics).items())),
        "weight": {
            "count": len(weights),
            "mean": sum(weights) / len(weights) if weights else 0.0,
            "min": min(weights, default=0.0),
            "max": max(weights, default=0.0),
        },
        "confidence_by_course": {
            c: {k: confidence[c][k] for k in _CONFIDENCE} for c in sorted(confidence)
        },
        # actual topic count minus budget; negative means under budget
        "budget_variance": {
            cid: courses.get(cid, 0) - c.budget
            for cid, c in sorted(kg.courses.items())
            if not c.is_view and (course is None or cid == course)
        },
    }


def _cross_subject(kg: KnowledgeGraph, tid: str, prereq: str) -> bool:
    p = kg.topics.get(prereq)
    return p is not None and _subject(p) != _subject(kg.topics[tid])


def review_report(kg: KnowledgeGraph, course: str | None = None) -> dict:
    topics = _scope(kg, course)
    low, cross = [], []
    for tid, t in topics.items():
        for e in t.prerequisites:
            if e.confidence == "low":
                low.append((tid, e.topic))
            if _cross_subject(kg, tid, e.topic):
                cross.append((tid, e.topic))
    return {
        "low_confidence": low,
        "near_limits": [tid for tid, t in topics.items() if is_near_limits(t)],
        "cross_subject": cross,
    }


@dataclass(frozen=True)
class QueueItem:
    topic: str
    prerequisite: str
    confidence: str
    descendants: int
    cross_subject: bool


def review_queue(
    kg: KnowledgeGraph, limit: int | None = None, course: str | None = None
) -> list[QueueItem]:
    """Edges to review: low confidence first, then most-depended-on topics, then cross-subject."""
    g = build_digraph(kg)
    items = []
    for tid, t in _scope(kg, course).items():
        if not t.prerequisites:
            continue
        n = len(nx.descendants(g, tid) - {tid})
        for e in t.prerequisites:
            items.append(QueueItem(tid, e.topic, e.confidence, n, _cross_subject(kg, tid, e.topic)))
    items.sort(
        key=lambda q: (
            q.confidence != "low",
            -q.descendants,
            not q.cross_subject,
            q.topic,
            q.prerequisite,
        )
    )
    return items if limit is None else items[:limit]


def _words(t: Topic) -> frozenset[str]:
    text = " ".join([t.name, *(k.can_do for k in t.knowledge_points)]).lower()
    return frozenset(_WORD.findall(text))


def find_duplicates(
    kg: KnowledgeGraph, threshold: float = 0.8, course: str | None = None
) -> list[tuple[str, str, float]]:
    """Cross-course topic pairs whose word sets have Jaccard similarity >= threshold.

    Topics with identical word sets are grouped, and candidates come from an inverted
    index over each set's rarest words (prefix filtering), so unrelated pairs are never compared.
    """
    groups: dict[frozenset[str], list[str]] = {}
    for tid, t in kg.topics.items():
        if not t.is_stub:
            ws = _words(t)
            if ws:
                groups.setdefault(ws, []).append(tid)
    freq = Counter(w for ws in groups for w in ws)
    ordered = {ws: sorted(ws, key=lambda w: (freq[w], w)) for ws in groups}
    eps = 1e-9

    def emit(xs: list[str], ys: list[str], score: float) -> None:
        for a in xs:
            for b in ys:
                ca, cb = _course(kg.topics[a]), _course(kg.topics[b])
                if a == b or ca == cb or (course and course not in (ca, cb)):
                    continue
                found.append((*sorted((a, b)), round(score, 4)))

    found: list[tuple[str, str, float]] = []
    index: dict[str, list[frozenset[str]]] = {}
    for ws in sorted(groups, key=lambda s: (len(s), sorted(s))):
        members = groups[ws]
        emit(members, members, 1.0)  # identical word sets (each pair appears twice; deduped below)
        n = len(ws)
        prefix = ordered[ws][: n - math.ceil(threshold * n - eps) + 1]
        seen: set[frozenset[str]] = set()
        for w in prefix:
            for other in index.get(w, ()):
                if other in seen:
                    continue
                seen.add(other)
                if len(other) < threshold * n - eps:
                    continue
                score = len(ws & other) / len(ws | other)
                if score >= threshold - eps:
                    emit(groups[other], members, score)
        for w in prefix:
            index.setdefault(w, []).append(ws)
    unique = sorted(set(found), key=lambda r: (-r[2], r[0], r[1]))
    return unique
