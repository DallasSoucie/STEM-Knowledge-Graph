"""Repeatable curriculum-bands layout: levels run left to right, subjects stack in rows."""

from collections import defaultdict

from kg.graph import KnowledgeGraph
from kg.model import LEVELS, level_rank

SUBJECT_ORDER = ("math", "physics", "chem", "bio", "engr")
ROW_LANES = 30
MIN_COLUMN_WIDTH = 20.0
WIDTH_PER_TOPIC = 0.5  # column width units per budgeted topic of the largest per-level share


def _subject_rows(kg: KnowledgeGraph) -> dict[str, int]:
    """Row index per subject: pinned order first, then any other subject in manifest order."""
    subjects = [c.subject for c in kg.courses.values()]
    subjects += [t.id.split(".")[0] for t in kg.topics.values()]
    extra = list(dict.fromkeys(s for s in subjects if s not in SUBJECT_ORDER))
    return {s: i for i, s in enumerate((*SUBJECT_ORDER, *extra))}


def lane_of(kg: KnowledgeGraph) -> dict[str, tuple[str, int]]:
    """course id -> (subject, lane). First-fit in manifest order; view courses get no lane."""
    taken: dict[str, list[list[tuple[int, int]]]] = defaultdict(list)
    result: dict[str, tuple[str, int]] = {}
    for c in kg.courses.values():
        if c.is_view:
            continue
        lo, hi = sorted(level_rank(x) for x in c.levels)
        lanes = taken[c.subject]
        for i, spans in enumerate(lanes):
            if all(hi < a or b < lo for a, b in spans):
                spans.append((lo, hi))
                lane = i
                break
        else:
            lane = len(lanes)
            lanes.append([(lo, hi)])
        if lane >= ROW_LANES:
            raise ValueError(
                f"subject {c.subject!r} needs more than {ROW_LANES} lanes (course {c.id})"
            )
        result[c.id] = (c.subject, lane)
    return result


def column_bounds(kg: KnowledgeGraph) -> dict[str, tuple[float, float]]:
    """level -> (x_start, x_end) for every level, widths driven by course budgets."""
    share = dict.fromkeys(LEVELS, 0.0)
    for c in kg.courses.values():
        if c.is_view:
            continue
        lo, hi = sorted(level_rank(x) for x in c.levels)
        per_level = c.budget / (hi - lo + 1)
        for r in range(lo, hi + 1):
            share[LEVELS[r]] = max(share[LEVELS[r]], per_level)
    bounds: dict[str, tuple[float, float]] = {}
    x = 0.0
    for level in LEVELS:
        width = max(MIN_COLUMN_WIDTH, share[level] * WIDTH_PER_TOPIC)
        bounds[level] = (x, x + width)
        x += width
    return bounds


def compute_positions(kg: KnowledgeGraph) -> dict[str, tuple[float, float]]:
    """topic id -> (x, y). Lane y is the row start plus lane plus 0.5."""
    rows = _subject_rows(kg)
    lanes = lane_of(kg)
    bounds = column_bounds(kg)

    def level_of(t) -> str:
        if t.level:
            return t.level
        c = kg.courses.get(t.course_id)
        return min(c.levels, key=level_rank) if c else LEVELS[0]

    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for t in kg.topics.values():
        groups[(t.course_id, level_of(t))].append(t.id)

    positions: dict[str, tuple[float, float]] = {}
    for (cid, level), ids in groups.items():
        subject, lane = lanes.get(cid, (cid.split(".")[0], 0))
        start, end = bounds[level]
        y = rows[subject] * ROW_LANES + lane + 0.5
        for i, tid in enumerate(ids):
            positions[tid] = (start + (i + 0.5) / len(ids) * (end - start), y)
    return positions
