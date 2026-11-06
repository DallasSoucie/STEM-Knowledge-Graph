"""Repeatable curriculum-bands layout: levels run left to right, subjects stack in rows."""

from collections import defaultdict
from math import ceil

from kg.graph import KnowledgeGraph
from kg.model import LEVELS, level_rank

SUBJECT_ORDER = ("math", "physics", "chem", "bio", "engr")
# Lanes each subject's row can hold. Fixed, so one subject's courses never move another's row.
LANE_CAPACITY = {"math": 12, "physics": 8, "chem": 8, "bio": 12, "engr": 30}
DEFAULT_LANE_CAPACITY = 12  # for a subject outside SUBJECT_ORDER

# A course's topics at one level form a block: left to right, then down, like lines of text.
LINES_PER_LANE = 8
LINE_SPACING = 1.0
TOPIC_SPACING = 4.0  # least spacing along a line at budget; wider than LINE_SPACING since names are wide
LANE_GAP = 2.0
LANE_HEIGHT = LINES_PER_LANE * LINE_SPACING + LANE_GAP
ROW_GAP = LANE_HEIGHT
COLUMN_PADDING = 2.0

MIN_COLUMN_WIDTH = 20.0
# Column width per budgeted topic of the largest per-level share, whose block gets TOPIC_SPACING.
WIDTH_PER_TOPIC = TOPIC_SPACING / LINES_PER_LANE


def _subject_rows(kg: KnowledgeGraph) -> dict[str, int]:
    """Row index per subject: pinned order first, then any other subject in manifest order."""
    subjects = [c.subject for c in kg.courses.values()]
    subjects += [t.id.split(".")[0] for t in kg.topics.values()]
    extra = list(dict.fromkeys(s for s in subjects if s not in SUBJECT_ORDER))
    return {s: i for i, s in enumerate((*SUBJECT_ORDER, *extra))}


def _capacity(subject: str) -> int:
    return LANE_CAPACITY.get(subject, DEFAULT_LANE_CAPACITY)


def row_bounds(kg: KnowledgeGraph) -> dict[str, tuple[float, float]]:
    """subject -> (y_start, y_end), each row as tall as its subject's lane capacity."""
    bounds: dict[str, tuple[float, float]] = {}
    y = 0.0
    for subject in _subject_rows(kg):
        bounds[subject] = (y, y + _capacity(subject) * LANE_HEIGHT)
        y = bounds[subject][1] + ROW_GAP
    return bounds


def _assign_lanes(kg: KnowledgeGraph) -> tuple[dict[str, tuple[str, int]], list[str]]:
    """First-fit lanes per course in manifest order, plus the courses that overflow their subject."""
    taken: dict[str, list[list[tuple[int, int]]]] = defaultdict(list)
    result: dict[str, tuple[str, int]] = {}
    overflow: list[str] = []
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
        if lane >= _capacity(c.subject):
            overflow.append(c.id)
        result[c.id] = (c.subject, lane)
    return result, overflow


def lane_overflows(kg: KnowledgeGraph) -> list[tuple[str, str]]:
    """(course id, subject) for every course that does not fit in its subject's lane capacity."""
    _, overflow = _assign_lanes(kg)
    return [(cid, kg.courses[cid].subject) for cid in overflow]


def lane_of(kg: KnowledgeGraph) -> dict[str, tuple[str, int]]:
    """course id -> (subject, lane). First-fit in manifest order; view courses get no lane."""
    result, overflow = _assign_lanes(kg)
    if overflow:
        subject = kg.courses[overflow[0]].subject
        raise ValueError(
            f"subject {subject!r} needs more than {_capacity(subject)} lanes (course {overflow[0]})"
        )
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
    """topic id -> (x, y). Each course and level is a block of lines across its column, in its lane.

    Line length comes from the course's budget, so at budget a block fills its lane and a course
    growing within budget only fills its own block. Past that, its lines tighten, never grow taller.
    """
    rows = row_bounds(kg)
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

    def budget_share(cid: str) -> float:
        c = kg.courses.get(cid)
        if c is None:
            return 0.0
        lo, hi = sorted(level_rank(x) for x in c.levels)
        return c.budget / (hi - lo + 1)

    positions: dict[str, tuple[float, float]] = {}
    for (cid, level), ids in groups.items():
        subject, lane = lanes.get(cid, (cid.split(".")[0], 0))
        start, end = bounds[level]
        width = end - start
        line_length = max(1, ceil(max(budget_share(cid), len(ids)) / LINES_PER_LANE))
        pitch = (width - COLUMN_PADDING) / line_length
        top = rows[subject][0] + lane * LANE_HEIGHT
        for i, tid in enumerate(ids):
            line, along = divmod(i, line_length)
            positions[tid] = (
                start + COLUMN_PADDING / 2 + (along + 0.5) * pitch,
                top + (line + 0.5) * LINE_SPACING,
            )
    return positions
