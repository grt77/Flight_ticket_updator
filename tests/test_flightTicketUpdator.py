import pytest
from src.FlightTicketUpdater import FlightTicketUpdater
import pandas as pd
import  test_data


@pytest.mark.parametrize("input,expected_output",test_data.test_cases_for_book_cabin_validation)
def test_book_cabin_validation(input,expected_output):
    ftu_obj=FlightTicketUpdater('test','2023-09-22')
    assert ftu_obj.book_cabin_validation(input).equals(expected_output)



@pytest.mark.parametrize("input,expected_output",test_data.test_cases_for_ticketing_date_validation)
def test_ticketing_date_validation(input,expected_output):
    ftu_obj=FlightTicketUpdater('test','2023-09-22')
    assert ftu_obj.ticketing_date_validation(input).equals(expected_output)



@pytest.mark.parametrize("input,expected_output",test_data.test_cases_for_applying_discount_validation)
def test_ticketing_discount_validation(input,expected_output):
    ftu_obj=FlightTicketUpdater('test','2023-09-22')
    assert ftu_obj.apply_discount_code(input).equals(expected_output)

