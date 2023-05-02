import pytest
from src.DateOperations import get_date_object_unformatted,get_date_obj_formatted
from datetime import date

test_cases_for_date_obj_unformatted=[('2022-09-22','2022-09-22'),('2023/22/09','2023-09-22'),('2022-09-09','None'),('202-08-01','None')]

test_cases_for_date_obj_formatted=[('2022-09-22','2022-09-22'),('2023/22/09','None'),('2022-09-19','2022-09-19'),('202-08-01','None')]


@pytest.mark.parametrize("input,expected_output",test_cases_for_date_obj_unformatted)
def test_get_date_object_unformatted(input,expected_output):
    assert str(get_date_object_unformatted(input))==expected_output



@pytest.mark.parametrize("input,expected_output",test_cases_for_date_obj_formatted)
def test_get_date_object_formatted(input,expected_output):
    assert str(get_date_obj_formatted(input))==expected_output


