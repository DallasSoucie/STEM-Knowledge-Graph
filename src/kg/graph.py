"""In-memory graph container, plus the prerequisite index and lineage queries."""

from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import networkx as nx

from kg.model import Course, HistoryEntry, Topic


@dataclass
class KnowledgeGraph:
    topics: dict[str, Topic] = field(default_factory=dict)  # insertion order is course order
    courses: dict[str, Course] = field(default_factory=dict)
    history: list[HistoryEntry] = field(default_factory=list)
    duplicate_ids: list[str] = field(default_factory=list)
    duplicate_courses: list[str] = field(default_factory=list)  # course IDs repeated in courses.yaml
    root: Path = Path("graph")


def build_digraph(kg: KnowledgeGraph) -> nx.DiGraph:
    """Edges run prerequisite -> topic, from `prerequisites` only; dangling targets are skipped."""
    g = nx.DiGraph()
    g.add_nodes_from(kg.topics)
    for tid, topic in kg.topics.items():
        for e in topic.prerequisites:
            if e.topic in kg.topics:
                g.add_edge(e.topic, tid)
    return g


class GraphIndex:
    """Ancestor closures as Python-int bitsets, computed once. Safe on cyclic graphs."""

    def __init__(self, kg: KnowledgeGraph):
        self.graph = build_digraph(kg)
        self._order = list(self.graph.nodes)
        self._index = {t: i for i, t in enumerate(self._order)}
        cond = nx.condensation(self.graph)
        mask: dict[int, int] = {}
        for c, data in cond.nodes(data=True):
            m = 0
            for t in data["members"]:
                m |= 1 << self._index[t]
            mask[c] = m
        self._comp = cond.graph["mapping"]
        self._mask = mask
        self._bits: dict[int, int] = {}
        for c in nx.topological_sort(cond):
            b = 0
            for p in cond.predecessors(c):
                b |= self._bits[p] | mask[p]
            self._bits[c] = b

    def cycles(self) -> list[list[str]]:
        """One representative cycle per strongly connected group (or self-loop)."""
        found = []
        for comp in nx.strongly_connected_components(self.graph):
            if len(comp) > 1 or any(self.graph.has_edge(t, t) for t in comp):
                sub = self.graph.subgraph(comp)
                found.append([u for u, _ in nx.find_cycle(sub)])
        return found

    def _ancestor_bits(self, tid: str) -> int:
        c = self._comp[tid]
        bits = self._bits[c]
        if self._mask[c] & (self._mask[c] - 1):  # more than one member: a cycle
            bits |= self._mask[c]
        return bits & ~(1 << self._index[tid])

    def is_ancestor(self, a: str, b: str) -> bool:
        if a not in self._index or b not in self._index or a == b:
            return False
        return bool(self._ancestor_bits(b) >> self._index[a] & 1)

    def ancestors(self, tid: str) -> set[str]:
        if tid not in self._index:
            return set()
        bits = self._ancestor_bits(tid)
        return {t for i, t in enumerate(self._order) if bits >> i & 1}

    def descendants(self, tid: str) -> set[str]:
        if tid not in self._index:
            return set()
        return nx.descendants(self.graph, tid) - {tid}


def lineage(
    kg: KnowledgeGraph,
    topic_id: str,
    direction: Literal["prerequisites", "dependents", "both"],
    max_steps: int | None,
) -> set[str]:
    """Topics reachable within max_steps edges (None = unlimited), excluding the topic itself."""
    g = build_digraph(kg)
    if topic_id not in g:
        return set()
    result: set[str] = set()
    if direction in ("prerequisites", "both"):
        result |= _walk(g, topic_id, g.predecessors, max_steps)
    if direction in ("dependents", "both"):
        result |= _walk(g, topic_id, g.successors, max_steps)
    return result - {topic_id}


def _walk(g: nx.DiGraph, start: str, step, max_steps: int | None) -> set[str]:
    """Nodes reached from start in one direction within max_steps edges."""
    seen = {start}
    queue = deque([(start, 0)])
    while queue:
        node, depth = queue.popleft()
        if max_steps is not None and depth >= max_steps:
            continue
        for n in step(node):
            if n not in seen:
                seen.add(n)
                queue.append((n, depth + 1))
    return seen


def shortest_path(kg: KnowledgeGraph, a: str, b: str) -> list[str] | None:
    """Shortest chain from prerequisite `a` up to dependent `b`, or None."""
    g = build_digraph(kg)
    if a not in g or b not in g:
        return None
    try:
        return nx.shortest_path(g, a, b)
    except nx.NetworkXNoPath:
        return None
