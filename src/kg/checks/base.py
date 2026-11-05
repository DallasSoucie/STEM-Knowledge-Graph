"""Issue type, rule registry and the runner."""

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Literal

import networkx as nx

from kg.graph import GraphIndex, KnowledgeGraph

Severity = Literal["error", "warning"]
COURSES_FILE_NAME = "courses.yaml"


@dataclass(frozen=True)
class Issue:
    severity: Severity
    rule: str
    topic: str | None
    file: str | None
    message: str


@dataclass(frozen=True)
class Rule:
    name: str
    severity: Severity
    fn: Callable[[KnowledgeGraph, GraphIndex], Iterable[Issue]]


RULES: dict[str, Rule] = {}


def rule(name: str, severity: Severity):
    """Register `fn(kg, index) -> Iterable[Issue]` under `name`."""

    def register(fn):
        if name in RULES:
            raise ValueError(f"duplicate rule name {name!r}")
        RULES[name] = Rule(name, severity, fn)
        return fn

    return register


def topic_file(topic_id: str) -> str | None:
    """`<subject>/<short>.yaml`, derived from the ID; None when the ID has no course part."""
    parts = topic_id.split(".")
    return f"{parts[0]}/{parts[1]}.yaml" if len(parts) >= 3 else None


def issue(rule_name: str, message: str, topic: str | None = None, file: str | None = None) -> Issue:
    """Build an Issue for a registered rule; the file defaults to the topic's course file."""
    if file is None and topic is not None:
        file = topic_file(topic)
    return Issue(RULES[rule_name].severity, rule_name, topic, file, message)


def is_acyclic(index: GraphIndex) -> bool:
    """Whether prerequisites form no cycle; ancestor-based rules skip otherwise. Cached."""
    cached = getattr(index, "_acyclic", None)
    if cached is None:
        cached = nx.is_directed_acyclic_graph(index.graph)
        index._acyclic = cached
    return cached


def run_checks(kg: KnowledgeGraph) -> list[Issue]:
    index = GraphIndex(kg)
    found: list[Issue] = []
    for r in RULES.values():
        found.extend(r.fn(kg, index))
    return found
