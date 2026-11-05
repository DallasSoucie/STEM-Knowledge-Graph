"""Weight CSV round trip. Import may change only `encompassing` and `confidence` of existing edges."""

import copy
import csv
import math
from pathlib import Path

from kg.graph import KnowledgeGraph
from kg.model import Edge

COLUMNS = ["topic", "kind", "prerequisite", "encompassing", "confidence"]
KINDS = ("direct", "encompassed")
CONFIDENCES = ("high", "medium", "low")


class WeightImportError(Exception):
    def __init__(self, problems: list[str]):
        self.problems = problems
        super().__init__("\n".join(problems))


def _edges(topic, kind: str) -> list[Edge]:
    return topic.prerequisites if kind == "direct" else topic.encompassed


def export_weights(kg: KnowledgeGraph, out: Path) -> None:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(COLUMNS)
        for t in kg.topics.values():
            for kind in KINDS:
                for e in _edges(t, kind):
                    writer.writerow([t.id, kind, e.topic, repr(e.encompassing), e.confidence])


def import_weights(kg: KnowledgeGraph, csv_path: Path) -> KnowledgeGraph:
    """Return a copy of kg with the CSV's weights applied; raise with every problem found."""
    with Path(csv_path).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = [h.strip() for h in next(reader, [])]
        if header != COLUMNS:
            raise WeightImportError([f"row 1: header must be {','.join(COLUMNS)}"])
        rows = [(n, [c.strip() for c in r]) for n, r in enumerate(reader, start=2)]

    out = copy.deepcopy(kg)
    problems: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    for n, cells in rows:
        if not any(cells):
            continue  # blank line, or Excel's trailing empty cells
        if len(cells) != len(COLUMNS):
            problems.append(f"row {n}: expected {len(COLUMNS)} columns, found {len(cells)}")
            continue
        topic_id, kind, target, weight_text, confidence = cells
        row_problems = []
        if kind not in KINDS:
            row_problems.append(f"kind must be direct or encompassed, not {kind!r}")
        if confidence not in CONFIDENCES:
            row_problems.append(f"confidence must be high, medium or low, not {confidence!r}")
        weight = None
        try:
            weight = float(weight_text)
            if not math.isfinite(weight) or not 0.0 <= weight <= 1.0:
                row_problems.append(f"encompassing {weight_text} is outside 0-1")
        except ValueError:
            row_problems.append(f"encompassing {weight_text!r} is not a number")
        edge = None
        if kind in KINDS:
            if topic_id not in out.topics:
                row_problems.append(f"unknown topic {topic_id}")
            else:
                edge = next((e for e in _edges(out.topics[topic_id], kind) if e.topic == target), None)
                if edge is None:
                    row_problems.append(f"no {kind} edge from {topic_id} to {target}")
        key = (topic_id, kind, target)
        if key in seen:
            row_problems.append("duplicate of an earlier row")
        seen.add(key)
        if row_problems:
            problems.extend(f"row {n}: {p}" for p in row_problems)
        elif edge is not None:
            edge.encompassing = weight
            edge.confidence = confidence
    if problems:
        raise WeightImportError(problems)
    return out
