"""Course-sequence rules: follows cycles, gaps, and the learner walk."""

import networkx as nx

from kg.checks.base import COURSES_FILE_NAME, issue, rule
from kg.graph import GraphIndex, KnowledgeGraph
from kg.limits import course_closure
from kg.model import Course


@rule("manifest-follows-cycle", "error")
def manifest_follows_cycle(kg: KnowledgeGraph, index: GraphIndex):
    g = nx.DiGraph()
    for c in kg.courses.values():
        g.add_node(c.id)
        g.add_edges_from((f, c.id) for f in c.follows if f in kg.courses)
    for comp in nx.strongly_connected_components(g):
        if len(comp) > 1 or any(g.has_edge(c, c) for c in comp):
            yield issue(
                "manifest-follows-cycle",
                f"courses follow each other in a cycle: {', '.join(sorted(comp))}",
                file=COURSES_FILE_NAME,
            )


class _Scope:
    """What a learner already has when starting `course`, plus its listed topic sequence."""

    def __init__(self, kg: KnowledgeGraph, course: Course, by_course: dict[str, list[str]]):
        self.closure = course_closure(kg, course.id)
        others = [kg.courses[c] for c in self.closure if c != course.id]
        self.other_courses = {c.id for c in others if not c.is_view}
        self.view_members = {t for c in others if c.is_view for t in c.view_topics or []}
        self.own_view = set(course.view_topics or [])
        if course.is_view:
            self.sequence = [t for t in course.view_topics or [] if t in kg.topics]
        else:
            self.sequence = by_course.get(course.id, [])


def _scopes(kg: KnowledgeGraph):
    by_course: dict[str, list[str]] = {}
    for tid, t in kg.topics.items():
        by_course.setdefault(t.course_id, []).append(tid)
    for course in kg.courses.values():
        yield course, _Scope(kg, course, by_course)


@rule("course-gap", "error")
def course_gap(kg: KnowledgeGraph, index: GraphIndex):
    for course, scope in _scopes(kg):
        for tid in scope.sequence:
            for e in kg.topics[tid].prerequisites:
                p = kg.topics.get(e.topic)
                if p is None:
                    continue  # reported as dangling-reference
                if (
                    p.course_id in scope.closure
                    or e.topic in scope.own_view
                    or e.topic in scope.view_members
                ):
                    continue
                yield issue(
                    "course-gap",
                    f"prerequisite {e.topic} (course {p.course_id}) is outside the courses "
                    f"that come before or make up {course.id}",
                    tid,
                )


@rule("learner-walk", "error")
def learner_walk(kg: KnowledgeGraph, index: GraphIndex):
    for course, scope in _scopes(kg):
        walked: set[str] = set()
        for tid in scope.sequence:
            for e in kg.topics[tid].prerequisites:
                p = kg.topics.get(e.topic)
                if p is None:
                    continue  # reported as dangling-reference
                if (
                    e.topic in walked
                    or p.course_id in scope.other_courses
                    or e.topic in scope.view_members
                ):
                    continue
                yield issue(
                    "learner-walk",
                    f"prerequisite {e.topic} is not yet known when {course.id} reaches this topic",
                    tid,
                )
            walked.add(tid)
