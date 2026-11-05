"""Graph schema. Models check types and required fields only; numeric limits belong to checks."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

LEVELS: tuple[str, ...] = (
    "gk",
    *(f"g{n}" for n in range(1, 13)),
    "uni-lower",
    "uni-upper",
)


def _check_level(level: str) -> str:
    if level not in LEVELS:
        raise ValueError(f"unknown level {level!r}; expected one of {', '.join(LEVELS)}")
    return level


def level_rank(level: str) -> int:
    return LEVELS.index(level)


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Edge(_Strict):
    topic: str
    encompassing: float
    confidence: Literal["high", "medium", "low"]


class KnowledgePoint(_Strict):
    id: str
    can_do: str
    key_prerequisites: list[str] = Field(default_factory=list)


class Topic(_Strict):
    id: str
    name: str
    status: Literal["stub", "draft", "reviewed"]
    subject: str | None = None
    course: str | None = None
    level: str | None = None
    justification: str | None = None
    prerequisites: list[Edge] = Field(default_factory=list)
    encompassed: list[Edge] = Field(default_factory=list)
    knowledge_points: list[KnowledgePoint] = Field(default_factory=list)

    @field_validator("level")
    @classmethod
    def _known_level(cls, v: str | None) -> str | None:
        return v if v is None else _check_level(v)

    @model_validator(mode="after")
    def _non_stub_needs_placement(self):
        if not self.is_stub and not (self.subject and self.course and self.level):
            raise ValueError("non-stub topic requires subject, course and level")
        return self

    @property
    def is_stub(self) -> bool:
        return self.status == "stub"

    @property
    def course_id(self) -> str:
        return ".".join(self.id.split(".")[:2])


class Course(_Strict):
    id: str
    subject: str
    levels: tuple[str, str]
    budget: int
    follows: list[str] = Field(default_factory=list)
    view_topics: list[str] | None = None

    @field_validator("levels")
    @classmethod
    def _known_levels(cls, v: tuple[str, str]) -> tuple[str, str]:
        for level in v:
            _check_level(level)
        return v

    @property
    def is_view(self) -> bool:
        return self.view_topics is not None


class HistoryEntry(_Strict):
    op: Literal["rename", "split"]
    source: str
    targets: list[str]
