"""In-memory graph container. Logic lives elsewhere; this is data only."""

from dataclasses import dataclass, field
from pathlib import Path

from kg.model import Course, HistoryEntry, Topic


@dataclass
class KnowledgeGraph:
    topics: dict[str, Topic] = field(default_factory=dict)  # insertion order is course order
    courses: dict[str, Course] = field(default_factory=dict)
    history: list[HistoryEntry] = field(default_factory=list)
    duplicate_ids: list[str] = field(default_factory=list)
    root: Path = Path("graph")
