import pytest
from pydantic import ValidationError

from kg.model import Edge, Topic, level_rank


def test_levels_are_ordered():
    assert level_rank("gk") < level_rank("g1") < level_rank("g12") < level_rank("uni-lower") < level_rank("uni-upper")


def test_unknown_keys_are_rejected():
    with pytest.raises(ValidationError):
        Topic.model_validate({"id": "math.k.a", "name": "A", "status": "stub", "statsu": "x"})


def test_stub_needs_only_id_name_status():
    t = Topic.model_validate({"id": "math.k.a", "name": "A", "status": "stub"})
    assert t.is_stub and t.course_id == "math.k"


def test_non_stub_requires_subject_course_level():
    with pytest.raises(ValidationError):
        Topic.model_validate({"id": "math.k.a", "name": "A", "status": "draft"})


def test_out_of_range_weight_loads_so_a_check_can_report_it():
    assert Edge(topic="x", encompassing=1.4, confidence="low").encompassing == 1.4
