"""Repeatable flow layout: stages run left to right by prerequisite depth, each level floored to the one before."""

from collections import defaultdict
from math import floor
from statistics import mean, quantiles

import networkx as nx

from kg.graph import KnowledgeGraph
from kg.model import LEVELS

SUBJECT_ORDER = ("math", "physics", "chem", "bio", "engr")

LINE_SPACING = 1.0
STAGE_SPACING = 3.0  # between stages; wider than LINE_SPACING for names, but the map is width-limited so more only flattens it


def _prerequisite_graph(kg: KnowledgeGraph) -> nx.DiGraph:
    """Direct prerequisites only; `encompassed` entries do not affect position."""
    g = nx.DiGraph()
    g.add_nodes_from(kg.topics)
    for t in kg.topics.values():
        g.add_edges_from((p.topic, t.id) for p in t.prerequisites if p.topic in kg.topics)
    return g


def topic_depths(kg: KnowledgeGraph) -> dict[str, int]:
    """Length of the longest prerequisite chain below each topic."""
    g = _prerequisite_graph(kg)
    depths: dict[str, int] = {}
    for tid in nx.lexicographical_topological_sort(g):
        depths[tid] = max((depths[p] + 1 for p in g.predecessors(tid)), default=0)
    return depths


def level_floors(kg: KnowledgeGraph, depths: dict[str, int]) -> dict[str, int]:
    """Earliest stage per level that has topics, so higher levels never sit left of lower ones."""
    by_level: dict[str, list[int]] = defaultdict(list)
    for t in kg.topics.values():
        if t.level and not t.is_stub:
            by_level[t.level].append(depths[t.id])
    floors: dict[str, int] = {}
    previous = -1
    for level in LEVELS:
        if level not in by_level:
            continue
        d = by_level[level]
        # quantiles needs two points; a lone topic is its own quartile
        quartile = floor(quantiles(d, n=4, method="inclusive")[0]) if len(d) > 1 else d[0]
        previous = 0 if previous < 0 else max(previous + 1, quartile)
        floors[level] = previous
    return floors


def topic_stages(kg: KnowledgeGraph) -> dict[str, int]:
    """Stage per topic: its level floor, pushed past the stage of every prerequisite."""
    g = _prerequisite_graph(kg)
    floors = level_floors(kg, topic_depths(kg))
    stages: dict[str, int] = {}
    for tid in nx.lexicographical_topological_sort(g):
        t = kg.topics[tid]
        start = floors[t.level] if t.level and not t.is_stub else 0
        stages[tid] = max([start, *(stages[p] + 1 for p in g.predecessors(tid))])
    return stages


def _group_keys(kg: KnowledgeGraph) -> dict[str, tuple]:
    """Per topic (subject rank, course rank); unknown subjects and courses sort last by name."""
    manifest = list(dict.fromkeys(c.subject for c in kg.courses.values()))
    courses = [c.id for c in kg.courses.values() if not c.is_view]

    def subject_rank(s: str) -> tuple:
        if s in SUBJECT_ORDER:
            return (0, SUBJECT_ORDER.index(s), "")
        return (1, manifest.index(s), "") if s in manifest else (2, 0, s)

    def course_rank(c: str) -> tuple:
        return (0, courses.index(c), "") if c in courses else (1, 0, c)

    return {
        t.id: (subject_rank(t.id.split(".")[0]), course_rank(t.course_id))
        for t in kg.topics.values()
    }


def flow_positions(kg: KnowledgeGraph) -> dict[str, tuple[float, float]]:
    """topic id -> (x, y). Stages run left to right; within a stage, subject then course then
    sweeps over prerequisites and dependents order the topics to cut crossings."""
    g = _prerequisite_graph(kg)
    stages = topic_stages(kg)
    group = _group_keys(kg)
    columns: dict[int, list[str]] = defaultdict(list)
    for tid in sorted(stages):
        columns[stages[tid]].append(tid)
    order = sorted(columns)

    position: dict[str, float] = {}

    def place(ids: list[str]) -> None:
        for i, tid in enumerate(ids):
            position[tid] = i - (len(ids) - 1) / 2

    for s in order:
        columns[s].sort(key=lambda t: (group[t], t))
        place(columns[s])

    for neighbours, stage_order in (
        (g.predecessors, order),
        (g.successors, order[::-1]),
        (g.predecessors, order),
        (g.successors, order[::-1]),
    ):
        for s in stage_order:
            def key(tid: str) -> tuple:
                near = [position[n] for n in neighbours(tid)]
                return (group[tid], mean(near) if near else position[tid], tid)

            columns[s].sort(key=key)
            place(columns[s])

    return {tid: (stages[tid] * STAGE_SPACING, position[tid] * LINE_SPACING) for tid in stages}
