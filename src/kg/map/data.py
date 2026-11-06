"""Plain-data view of a graph for the map page. No HTML here."""

from kg.graph import KnowledgeGraph
from kg.limits import is_near_limits
from kg.map.layout import (
    SUBJECT_ORDER,
    STAGE_SPACING,
    flow_positions,
    level_floors,
    topic_depths,
)
from kg.model import LEVELS


def _level_of(kg: KnowledgeGraph, t) -> str:
    """A stub has no level of its own, so it shows its course's first one."""
    if t.level:
        return t.level
    c = kg.courses.get(t.course_id)
    return c.levels[0] if c else LEVELS[0]


def build_map_data(kg: KnowledgeGraph) -> dict:
    """Levels, subjects, courses, level markers, topics with positions, and weighted edges."""
    positions = flow_positions(kg)
    floors = level_floors(kg, topic_depths(kg))
    used = {t.id.split(".")[0] for t in kg.topics.values()} | {c.subject for c in kg.courses.values()}
    # pinned subjects first, then any other in manifest order
    manifest = dict.fromkeys(c.subject for c in kg.courses.values())
    manifest.update(dict.fromkeys(t.id.split(".")[0] for t in kg.topics.values()))
    ordered = [*SUBJECT_ORDER, *(s for s in manifest if s not in SUBJECT_ORDER)]
    subjects = [{"id": s} for s in ordered if s in used]

    topics, index = [], {}
    for tid, t in kg.topics.items():
        x, y = positions[tid]
        index[tid] = len(topics)
        topics.append(
            {
                "id": tid,
                "name": t.name,
                "subject": t.subject or tid.split(".")[0],
                "course": t.course or t.course_id,
                "level": _level_of(kg, t),
                "status": t.status,
                "x": x,
                "y": y,
                "near_limits": is_near_limits(t),
                "kps": [
                    {"id": k.id, "can_do": k.can_do, "key_prerequisites": list(k.key_prerequisites)}
                    for k in t.knowledge_points
                ],
            }
        )

    edges = []
    for tid, t in kg.topics.items():
        for kind, group in (("direct", t.prerequisites), ("encompassed", t.encompassed)):
            for e in group:
                if e.topic in index:
                    edges.append([index[e.topic], index[tid], e.encompassing, e.confidence, kind])

    courses = [
        {
            "id": c.id,
            "subject": c.subject,
            "levels": list(c.levels),
            "budget": c.budget,
            "is_view": c.is_view,
        }
        for c in kg.courses.values()
    ]
    level_markers = [{"level": lv, "x": f * STAGE_SPACING} for lv, f in floors.items()]
    return {
        "levels": list(LEVELS),
        "subjects": subjects,
        "courses": courses,
        "level_markers": level_markers,
        "stage_spacing": STAGE_SPACING,
        "topics": topics,
        "edges": edges,
    }
