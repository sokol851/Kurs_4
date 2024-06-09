import pytest
from src.work_with_vacancies import Vacancies
import os
from config import ROOT_DIR
import json


@pytest.fixture
def vacancy():
    return Vacancies('Грузчик', '20000', '50000', 'RUR', 'СПб',
                     'Выносливый', 'http://hh.ru/1')


@pytest.fixture
def read_json():
    data = os.path.join(ROOT_DIR, 'tests', 'test_data', 'test_vacancies_read.json')
    with open(data, 'r', encoding="utf8") as file:
        vac_list = json.load(file)
        return vac_list


def test_repr(vacancy):
    assert vacancy.__repr__() == "Vacancies('Грузчик','20000','50000','RUR','СПб','Выносливый','http://hh.ru/1')"


def test_str(vacancy):
    assert vacancy.__str__() == (f'Вакансия: Грузчик\n'
                                 f'Заработная плата: от 20000 до 50000 RUR\n'
                                 f'Местоположение: СПб\n'
                                 f'Требования: Выносливый\n'
                                 f'Сcылка на ваканисию: http://hh.ru/1')


def test_to_json(vacancy):
    assert vacancy.to_json().__repr__() == ("Vacancies('Грузчик','20000','50000','RUR','СПб','Выносливый',"
                                            "'http://hh.ru/1')")


def test_create_vacancies(vacancy, read_json):
    data = read_json
    list_vac = [data[0]]
    assert (vacancy.create_vacancies(list_vac)[0].__str__() ==
            (f'Вакансия: Middle Python Developer\n'
             f'Заработная плата: от 150000 до 250000 RUR\n'
             f'Местоположение: Москва\n'
             f'Требования: Опыт написания кода на Django (+ DRF) от 2х лет. Понимание способов оптимизации SQL '
             f'запросов к БД. \n'
             f'Сcылка на ваканисию: https://hh.ru/vacancy/100523092'))
