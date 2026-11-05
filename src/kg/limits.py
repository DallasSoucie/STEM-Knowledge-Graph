"""Spec limits shared by validation and review reports, plus course-sequence helpers."""

from kg.graph import KnowledgeGraph
from kg.model import Topic


def is_near_limits(topic: Topic) -> bool:
    """4+ direct prerequisites, a KP with 4 key prerequisites, 2 or 5 KPs, or every KP at 3+."""
    if topic.is_stub:
        return False
    kps = topic.knowledge_points
    return (
        len(topic.prerequisites) >= 4
        or any(len(k.key_prerequisites) >= 4 for k in kps)
        or len(kps) in (2, 5)
        or (bool(kps) and all(len(k.key_prerequisites) >= 3 for k in kps))
    )


def course_closure(kg: KnowledgeGraph, course_id: str) -> set[str]:
    """The course plus every course it follows, transitively. Cycle- and unknown-ID-safe."""
    seen = {course_id}
    stack = [course_id]
    while stack:
        course = kg.courses.get(stack.pop())
        if course is None:
            continue
        for f in course.follows:
            if f in kg.courses and f not in seen:
                seen.add(f)
                stack.append(f)
    return seen
