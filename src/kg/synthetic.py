"""Deterministic synthetic graphs for speed and layout testing. Not real curriculum content."""

import random
from pathlib import Path

from kg.graph import KnowledgeGraph
from kg.model import LEVELS, Course, Edge, KnowledgePoint, Topic

SUBJECTS = ("math", "physics", "chem", "bio", "engr")
_MAX_COURSES_PER_SUBJECT = 30
_TOPICS_PER_COURSE = 120

_ADJECTIVES = (
    "basic", "advanced", "applied", "linear", "relative", "discrete", "average", "composite",
    "periodic", "angular", "net", "standard", "partial", "total", "ideal", "dynamic",
)
_NOUNS = (
    "rates", "ratios", "vectors", "forces", "energy", "charge", "waves", "fields", "cells",
    "bonds", "loads", "signals", "growth", "balance", "motion", "gradients", "models", "pairs",
)
_CONTEXTS = (
    "in one step", "with units", "from data", "in context", "with symbols", "by estimation",
    "in two dimensions", "with graphs", "for systems", "from first principles",
)


def _split(total: int, parts: int) -> list[int]:
    base, extra = divmod(total, parts)
    return [base + (1 if i < extra else 0) for i in range(parts)]


def _course_plan(n_topics: int) -> dict[str, list[int]]:
    """Course sizes per subject, in course order."""
    plan: dict[str, list[int]] = {}
    for subject, share in zip(SUBJECTS, _split(n_topics, len(SUBJECTS))):
        n_courses = max(1, min(_MAX_COURSES_PER_SUBJECT, round(share / _TOPICS_PER_COURSE), share))
        plan[subject] = [s for s in _split(share, n_courses) if s > 0]
    return plan


def _edge(rng: random.Random, target: str) -> Edge:
    return Edge(
        topic=target,
        encompassing=round(rng.uniform(0.05, 0.95), 2),
        confidence=rng.choices(("high", "medium", "low"), (6, 3, 1))[0],
    )


def generate(n_topics: int, seed: int = 0, root: Path = Path("graph")) -> KnowledgeGraph:
    """A valid graph of n_topics (at least 5) across five subjects; same seed, same graph."""
    rng = random.Random(seed)
    kg = KnowledgeGraph(root=Path(root))
    plan = _course_plan(n_topics)
    chain = {s: [f"{s}.c{k + 1:02d}" for k in range(len(sizes))] for s, sizes in plan.items()}
    ids_by_course: dict[str, list[str]] = {}
    prereq_ids: dict[str, list[str]] = {}

    for subject, sizes in plan.items():  # math is first in SUBJECTS
        m = len(sizes)
        for k, size in enumerate(sizes):
            cid = chain[subject][k]
            if k > 0:
                follows = [chain[subject][k - 1]]
            elif subject != "math":
                follows = [chain["math"][min(2, len(chain["math"]) - 1)]]
            else:
                follows = []
            lo = 1 + k * (len(LEVELS) - 2) // m
            hi = 1 + (k + 1) * (len(LEVELS) - 2) // m
            kg.courses[cid] = Course(
                id=cid, subject=subject, levels=(LEVELS[lo], LEVELS[hi]), budget=size, follows=follows
            )
            ids_by_course[cid] = []

    for cid, c in kg.courses.items():
        lo, hi = (LEVELS.index(x) for x in c.levels)
        own = ids_by_course[cid]
        other = ids_by_course[c.follows[0]] if c.follows else []
        for i in range(c.budget):
            words = f"{rng.choice(_ADJECTIVES)} {rng.choice(_NOUNS)} {rng.choice(_CONTEXTS)}"
            tid = f"{cid}.{words.replace(' ', '-')}-{i}"
            name = words.capitalize()

            k = rng.choices((1, 2, 3, 4), (2, 3, 3, 2))[0]
            chosen: list[str] = []
            if i == 1 and not other:
                chosen.append(own[0])  # keeps the course's first topic from being an orphan
            for _ in range(k * 3):
                if len(chosen) >= k:
                    break
                if other and (not own or rng.random() < (0.5 if i < 3 else 0.12)):
                    pick = rng.choice(other)
                elif own:  # recent topics are likelier prerequisites
                    pick = own[max(0, len(own) - 1 - int(rng.expovariate(1 / 12)))]
                else:
                    continue
                if pick not in chosen:
                    chosen.append(pick)
            prereq_ids[tid] = chosen

            # encompassed: grandparents, which are always real ancestors and not direct prerequisites
            grand = [g for p in chosen for g in prereq_ids[p] if g not in chosen]
            grand = list(dict.fromkeys(grand))
            rng.shuffle(grand)
            enc = grand[: rng.choice((1, 2, 3, 4))]

            weighted = chosen + enc
            kps = [
                KnowledgePoint(
                    id=f"kp{j}",
                    can_do=f"Do step {j} of {name.lower()}",
                    key_prerequisites=rng.sample(weighted, min(len(weighted), rng.choice((0, 1, 2)))),
                )
                for j in range(1, (3 if rng.random() < 0.6 else 4) + 1)
            ]
            kg.topics[tid] = Topic(
                id=tid,
                name=name,
                status="draft",
                subject=c.subject,
                course=cid,
                level=LEVELS[lo + (hi - lo) * i // max(1, c.budget - 1)],
                prerequisites=[_edge(rng, p) for p in chosen],
                encompassed=[_edge(rng, p) for p in enc],
                knowledge_points=kps,
            )
            own.append(tid)
    return kg
