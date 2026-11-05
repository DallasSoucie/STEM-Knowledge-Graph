"""Plain-data view of a graph for the map page. No HTML here."""

from kg.graph import KnowledgeGraph
from kg.limits import is_near_limits
from kg.map.layout import _subject_rows, column_bounds, compute_positions, lane_of, row_bounds
from kg.model import LEVELS


def _level_at(bounds: dict[str, tuple[float, float]], x: float) -> str:
    for level in LEVELS:
        if x < bounds[level][1]:
            return level
    return LEVELS[-1]


def build_map_data(kg: KnowledgeGraph) -> dict:
    """Levels, subject rows, courses, columns, topics with positions, and weighted edges."""
    positions = compute_positions(kg)
    bounds = column_bounds(kg)
    lanes = lane_of(kg)
    rows = _subject_rows(kg)
    row_ys = row_bounds(kg)
    used = {t.id.split(".")[0] for t in kg.topics.values()} | {c.subject for c in kg.courses.values()}
    subjects = [
        {"id": s, "row": r, "y0": row_ys[s][0], "y1": row_ys[s][1]}
        for s, r in sorted(rows.items(), key=lambda kv: kv[1])
        if s in used
    ]

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
                "level": t.level or _level_at(bounds, x),
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
            "lane": lanes[c.id][1] if c.id in lanes else None,
            "is_view": c.is_view,
        }
        for c in kg.courses.values()
    ]
    columns = [{"level": lv, "x0": bounds[lv][0], "x1": bounds[lv][1]} for lv in LEVELS]
    return {
        "levels": list(LEVELS),
        "subjects": subjects,
        "courses": courses,
        "columns": columns,
        "topics": topics,
        "edges": edges,
    }
