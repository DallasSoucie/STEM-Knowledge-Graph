"""Safe structural edits. Each returns a new graph; `apply_edit` writes only a valid result."""

import copy
import re

from kg.checks import Issue, run_checks
from kg.graph import KnowledgeGraph
from kg.model import Edge, HistoryEntry, KnowledgePoint, Topic
from kg.store import write_graph


class EditError(Exception):
    """The edit cannot be built at all (unknown or clashing ID); nothing was changed."""


def _swap(ids: list[str], old: str, new: str) -> list[str]:
    return [new if i == old else i for i in ids]


def _retarget(e: Edge, old: str, new: str) -> Edge:
    return e.model_copy(update={"topic": new}) if e.topic == old else e


def _same_course(old: str, new: str) -> bool:
    return old.split(".")[:2] == new.split(".")[:2]


def rename_id(kg: KnowledgeGraph, old: str, new: str) -> KnowledgeGraph:
    if old not in kg.topics:
        raise EditError(f"unknown topic: {old}")
    if new in kg.topics:
        raise EditError(f"topic already exists: {new}")
    if not _same_course(old, new):
        raise EditError(f"rename must stay inside course {kg.topics[old].course_id}: {new}")
    out = copy.deepcopy(kg)
    topics: dict[str, Topic] = {}
    for tid, t in out.topics.items():
        t.prerequisites = [_retarget(e, old, new) for e in t.prerequisites]
        t.encompassed = [_retarget(e, old, new) for e in t.encompassed]
        for kp in t.knowledge_points:
            kp.key_prerequisites = _swap(kp.key_prerequisites, old, new)
        if tid == old:
            t.id = new
        topics[new if tid == old else tid] = t  # rebuilt so course order is kept
    out.topics = topics
    for c in out.courses.values():
        if c.view_topics is not None:
            c.view_topics = _swap(c.view_topics, old, new)
    out.history.append(HistoryEntry(op="rename", source=old, targets=[new]))
    return out


def _next_kp_number(topic: Topic) -> int:
    numbers = [int(m.group(1)) for kp in topic.knowledge_points if (m := re.search(r"(\d+)$", kp.id))]
    return max(numbers, default=0) + 1


def split_topic(
    kg: KnowledgeGraph,
    topic_id: str,
    new_id: str,
    new_name: str,
    move_kps: list[str],
    keep_new_kps: list[str] = [],  # noqa: B006 - never mutated
    new_kps: list[str] = [],  # noqa: B006 - never mutated
) -> KnowledgeGraph:
    if topic_id not in kg.topics:
        raise EditError(f"unknown topic: {topic_id}")
    if new_id in kg.topics:
        raise EditError(f"topic already exists: {new_id}")
    if not _same_course(topic_id, new_id):
        raise EditError(f"new topic must stay inside course {kg.topics[topic_id].course_id}: {new_id}")
    src = kg.topics[topic_id]
    if src.is_stub:
        raise EditError(f"cannot split a stub: {topic_id}")
    have = {kp.id for kp in src.knowledge_points}
    missing = [k for k in move_kps if k not in have]
    if missing:
        raise EditError(f"{topic_id} has no knowledge point: {', '.join(missing)}")

    out = copy.deepcopy(kg)
    orig = out.topics[topic_id]
    moved = [kp for kp in orig.knowledge_points if kp.id in move_kps]
    kept = [kp for kp in orig.knowledge_points if kp.id not in move_kps]
    n = _next_kp_number(orig)
    for text in keep_new_kps:
        kept.append(KnowledgePoint(id=f"kp{n}", can_do=text))
        n += 1
    for text in new_kps:
        moved.append(KnowledgePoint(id=f"kp{n}", can_do=text))
        n += 1
    orig.knowledge_points = kept

    new = Topic(
        id=new_id,
        name=new_name,
        status="draft",
        subject=orig.subject,
        course=orig.course,
        level=orig.level,
        prerequisites=[Edge(topic=topic_id, encompassing=0.5, confidence="low")],
        knowledge_points=moved,
    )

    # moved KPs keep their key prerequisites, which must be weighted on the new topic too
    weights = {e.topic: e for e in orig.encompassed + orig.prerequisites}
    for kp in moved:
        for key in kp.key_prerequisites:
            if key != topic_id and key in weights and key not in {e.topic for e in new.encompassed}:
                new.encompassed.append(
                    Edge(topic=key, encompassing=weights[key].encompassing, confidence="low")
                )

    def repoint(edges: list[Edge]) -> list[Edge]:
        return [
            Edge(topic=new_id, encompassing=e.encompassing, confidence="low")
            if e.topic == topic_id
            else e
            for e in edges
        ]

    for t in out.topics.values():
        t.prerequisites = repoint(t.prerequisites)
        t.encompassed = repoint(t.encompassed)
        for kp in t.knowledge_points:
            kp.key_prerequisites = _swap(kp.key_prerequisites, topic_id, new_id)

    topics: dict[str, Topic] = {}
    for tid, t in out.topics.items():
        topics[tid] = t
        if tid == topic_id:
            topics[new_id] = new  # right after the original
    out.topics = topics
    out.history.append(HistoryEntry(op="split", source=topic_id, targets=[topic_id, new_id]))
    return out


def apply_edit(new_kg: KnowledgeGraph) -> list[Issue]:
    """Write the graph only if it has no errors; otherwise return the errors and write nothing."""
    errors = [i for i in run_checks(new_kg) if i.severity == "error"]
    if not errors:
        write_graph(new_kg)
    return errors
