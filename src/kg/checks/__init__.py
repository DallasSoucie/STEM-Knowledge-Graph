"""Validation rules. Importing this package registers every rule."""

from kg.checks import quality, sequence, structure  # noqa: F401 - imported to register rules
from kg.checks.base import RULES, Issue, Rule, rule, run_checks

__all__ = ["RULES", "Issue", "Rule", "rule", "run_checks"]
