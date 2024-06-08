import pytest
from src.api_service import WorkingHH


@pytest.fixture
def working_hh():
    return WorkingHH()


def test_get_vacancies(working_hh):
    assert len(working_hh.get_vacancies('Python', 10)) == 10


def test_input_get_vacancies(working_hh):
    pytest.raises(KeyError, working_hh.get_vacancies, 1, 'fff')


def test_input_get_vacancies_2(working_hh):
    assert working_hh.get_vacancies('Python', 0) == []
