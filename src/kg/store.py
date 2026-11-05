"""Canonical YAML store. All graph YAML reads and writes go through this module."""

from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from kg.graph import KnowledgeGraph
from kg.model import Course, Edge, HistoryEntry, KnowledgePoint, Topic

COURSES_FILE = "courses.yaml"
HISTORY_FILE = "id-history.yaml"

_Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


class GraphLoadError(Exception):
    def __init__(self, problems: list[tuple[Path, str]]):
        self.problems = problems
        super().__init__("\n".join(f"{p}: {msg}" for p, msg in problems))


class _FlowList(list):
    """A list dumped as `[a, b]` on one line."""


class _Dumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)  # indent list items under their key


_Dumper.add_representer(
    _FlowList, lambda d, data: d.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)
)


def _dump(data: dict) -> bytes:
    text = yaml.dump(
        data,
        Dumper=_Dumper,
        sort_keys=False,
        allow_unicode=True,
        width=float("inf"),
        default_flow_style=False,
    )
    return text.encode("utf-8")


def _edge(e: Edge) -> dict[str, Any]:
    return {"topic": e.topic, "encompassing": e.encompassing, "confidence": e.confidence}


def _kp(kp: KnowledgePoint) -> dict[str, Any]:
    d: dict[str, Any] = {"id": kp.id, "can_do": kp.can_do}
    if kp.key_prerequisites:
        d["key_prerequisites"] = _FlowList(kp.key_prerequisites)
    return d


def _topic(t: Topic) -> dict[str, Any]:
    d: dict[str, Any] = {"id": t.id, "name": t.name}
    for key in ("subject", "course", "level", "status", "justification"):
        value = getattr(t, key)
        if value is not None:
            d[key] = value
    if t.prerequisites:
        d["prerequisites"] = [_edge(e) for e in t.prerequisites]
    if t.encompassed:
        d["encompassed"] = [_edge(e) for e in t.encompassed]
    if t.knowledge_points:
        d["knowledge_points"] = [_kp(k) for k in t.knowledge_points]
    return d


def _course(c: Course) -> dict[str, Any]:
    d: dict[str, Any] = {
        "id": c.id,
        "subject": c.subject,
        "levels": _FlowList(c.levels),
        "budget": c.budget,
    }
    if c.follows:
        d["follows"] = list(c.follows)
    if c.view_topics is not None:
        d["view_topics"] = list(c.view_topics)
    return d


def _course_path(root: Path, course_id: str) -> Path:
    subject, short = course_id.split(".", 1)
    return Path(root) / subject / f"{short}.yaml"


def _write_if_changed(path: Path, data: bytes) -> None:
    if path.exists() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_course(root: Path, course_id: str, topics: list[Topic]) -> None:
    data = _dump({"course": course_id, "topics": [_topic(t) for t in topics]})
    _write_if_changed(_course_path(root, course_id), data)


def write_graph(kg: KnowledgeGraph) -> None:
    by_course: dict[str, list[Topic]] = {}
    for t in kg.topics.values():
        by_course.setdefault(t.course_id, []).append(t)
    for course_id, topics in by_course.items():
        write_course(kg.root, course_id, topics)
    _write_if_changed(
        Path(kg.root) / COURSES_FILE,
        _dump({"courses": [_course(c) for c in kg.courses.values()]}),
    )
    if kg.history:
        _write_if_changed(
            Path(kg.root) / HISTORY_FILE,
            _dump({"history": [h.model_dump() for h in kg.history]}),
        )


def _read_yaml(path: Path) -> Any:
    return yaml.load(path.read_bytes().decode("utf-8"), Loader=_Loader)


def _describe(exc: Exception) -> str:
    if isinstance(exc, ValidationError):
        return "; ".join(
            f"{'.'.join(str(p) for p in err['loc']) or '<root>'}: {err['msg']}"
            for err in exc.errors()
        )
    return " ".join(str(exc).split())


def _load_list(path: Path, key: str, model, problems: list[tuple[Path, str]]) -> list:
    """Read `<key>: [...]` from path and build models; record problems instead of raising."""
    try:
        doc = _read_yaml(path)
        if not isinstance(doc, dict) or not isinstance(doc.get(key), list):
            raise ValueError(f"expected a mapping with a '{key}' list")
        return [model.model_validate(item) for item in doc[key]]
    except Exception as exc:  # noqa: BLE001 - every failure becomes a reported problem
        problems.append((path, _describe(exc)))
        return []


def load_graph(root: Path) -> KnowledgeGraph:
    root = Path(root)
    problems: list[tuple[Path, str]] = []
    if not root.is_dir():
        raise GraphLoadError([(root, "graph directory not found")])

    kg = KnowledgeGraph(root=root)

    courses_path = root / COURSES_FILE
    if courses_path.exists():
        for c in _load_list(courses_path, "courses", Course, problems):
            kg.courses[c.id] = c

    history_path = root / HISTORY_FILE
    if history_path.exists():
        kg.history = _load_list(history_path, "history", HistoryEntry, problems)

    per_course: dict[str, list[Topic]] = {}
    for path in sorted(root.glob("*/*.yaml")):
        try:
            doc = _read_yaml(path)
            if not isinstance(doc, dict) or not isinstance(doc.get("course"), str):
                raise ValueError("expected a mapping with a 'course' id")
            if not isinstance(doc.get("topics"), list):
                raise ValueError("expected a 'topics' list")
            topics = [Topic.model_validate(item) for item in doc["topics"]]
            stray = [t.id for t in topics if t.course_id != doc["course"]]
            if stray:
                raise ValueError(
                    f"file declares course {doc['course']} but holds topics of other courses: "
                    + ", ".join(stray)
                )
        except Exception as exc:  # noqa: BLE001
            problems.append((path, _describe(exc)))
            continue
        per_course.setdefault(doc["course"], []).extend(topics)

    if problems:
        raise GraphLoadError(problems)

    # courses.yaml order first, then any unlisted course files in name order
    order = [c for c in kg.courses if c in per_course]
    order += [c for c in per_course if c not in kg.courses]
    for course_id in order:
        for t in per_course[course_id]:
            if t.id in kg.topics:
                kg.duplicate_ids.append(t.id)
            else:
                kg.topics[t.id] = t
    return kg
