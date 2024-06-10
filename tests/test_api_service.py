import pytest
from src.api_service import WorkingHH
import requests


@pytest.fixture
def working_hh():
    return WorkingHH()


def test_status_api():
    url_get = "https://api.hh.ru/vacancies"  # используемый адрес для отправки запроса
    response = requests.get(url_get)  # отправка GET-запроса
    assert response.status_code == 200


def test_get_vacancies(working_hh):
    list_vac = working_hh.get_vacancies('Python', 10)
    assert len(list_vac) == 10  # Проверка, что длина списка соответствует запрошеному кол-ву.
    assert list_vac[0].get('id') is not None  # Проверка, что id не пуст, а значит API сработало верно.


def test_input_get_vacancies(working_hh):
    pytest.raises(KeyError, working_hh.get_vacancies, 'Python', 'Не верное кол-во')  # Проверка на ввод str вместо int.


def test_input_get_vacancies_2(working_hh):
    assert working_hh.get_vacancies('Python', 0) == []
