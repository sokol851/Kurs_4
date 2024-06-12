import pytest
from src.work_with_file import WorkWithJSON
import os
from config import ROOT_DIR


@pytest.fixture
def create_exemplar():
    return WorkWithJSON('test_vacancies.json')


@pytest.fixture
def path_for_tests_read_original(create_exemplar):
    create_exemplar._path = os.path.join(f'{ROOT_DIR}/data/vacancies.json')


@pytest.fixture
def path_for_tests_read(create_exemplar):
    create_exemplar._path = os.path.join(f'{ROOT_DIR}/tests/test_data/test_vacancies_read.json')


@pytest.fixture
def path_for_tests_write(create_exemplar):
    create_exemplar._path = os.path.join(f'{ROOT_DIR}/tests/test_data/test_vacancies_write.json')


@pytest.fixture
def data():
    return [{'id': '1'}, {'id': '2'}, {'id': '3'}], [{'name': '1', 'alternate_url': '4'}], [{'id'}], {'id': 'added'}


def test_availability_json(path_for_tests_read_original):
    exemplar = WorkWithJSON('vacancies.json')
    assert exemplar.read_vacancy() is not None
    backup_list = exemplar.read_vacancy()
    # Удаляем файл, убеждаемся, что программа создала его сама при инициализации.
    os.remove(f'{ROOT_DIR}/data/vacancies.json')
    exemplar = WorkWithJSON('vacancies.json')
    assert exemplar.read_vacancy() is not None
    # Удаляем директорию, убеждаемся, что программа создала его сама при инициализации.
    os.remove(f'{ROOT_DIR}/data/vacancies.json')
    os.rmdir(f'{ROOT_DIR}/data')
    exemplar = WorkWithJSON('vacancies.json')
    assert exemplar.read_vacancy() is not None
    exemplar.write_vacancy(backup_list)


def test_read_work_with_json(create_exemplar, path_for_tests_read):
    assert create_exemplar.read_vacancy()[0]['name'] == 'Middle Python Developer'
    assert create_exemplar.read_vacancy()[1]['salary']['from'] == 280000
    assert create_exemplar.read_vacancy()[1].get('salary').get('to') is None
    with pytest.raises(AttributeError):
        create_exemplar.read_vacancy()[3].get('salary').get('to')


def test_write_work_with_json(create_exemplar, data, path_for_tests_write):
    create_exemplar.write_vacancy(data[0])
    assert len(create_exemplar.read_vacancy()) == len(data[0])
    with pytest.raises(TypeError):
        create_exemplar.write_vacancy(data[2])


def test_add_vacancy(create_exemplar, data, path_for_tests_write):
    create_exemplar.write_vacancy([])
    len_list = len(create_exemplar.read_vacancy())
    create_exemplar.add_vacancy(data[1], '4')
    assert len(create_exemplar.read_vacancy()) == len_list + len(data[1])
    with pytest.raises(KeyError):
        create_exemplar.add_vacancy(data[0], '2')


def test_del_vacancy(create_exemplar, path_for_tests_write, data):
    create_exemplar.write_vacancy(data[1])
    len_list = len(create_exemplar.read_vacancy())
    url = '4'
    create_exemplar.del_vacancy('4')
    assert len(create_exemplar.read_vacancy()) == len_list - len(url)
    with pytest.raises(AttributeError):
        create_exemplar.del_vacancy(4)


def test_del_clear_json(create_exemplar, path_for_tests_write, data):
    create_exemplar.write_vacancy(data[1])
    create_exemplar.clear_json()
    assert len(create_exemplar.read_vacancy()) == 0


def test_ask_to_write(create_exemplar, data, path_for_tests_write, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'да')
    create_exemplar.ask_to_write(data[0])
    assert create_exemplar.read_vacancy() == data[0]
    create_exemplar.ask_to_write(data[1])
    assert create_exemplar.read_vacancy() == data[1]
    create_exemplar.ask_to_write([])
    assert len(create_exemplar.read_vacancy()) == 0


def test_filter_by_keyword(create_exemplar, path_for_tests_read):
    assert create_exemplar.filter_by_keyword('sql, python')[0]['id'] == '100523092'
    with pytest.raises(IndexError):
        print(create_exemplar.filter_by_keyword('sql, python')[3])
    with pytest.raises(AttributeError):
        print(create_exemplar.filter_by_keyword(1))
    assert create_exemplar.filter_by_keyword('None_key_in_list') == []


def test_filter_by_salary(create_exemplar, path_for_tests_read, monkeypatch):
    assert create_exemplar.filter_by_salary('280000')[0]['salary']['from'] == 280000
    with pytest.raises(AttributeError):
        create_exemplar.filter_by_salary(280000)
    assert create_exemplar.filter_by_salary('99999999999999999999') == []
    answers = iter(['', '0'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    assert create_exemplar.filter_by_salary('') == create_exemplar.read_vacancy()


def test_filter_by_area(create_exemplar, path_for_tests_read):
    assert create_exemplar.filter_by_area('МоСкВа')[0]['id'] == '100523092'
    assert create_exemplar.filter_by_area('МоСкВа')[0]['area']['name'] == 'Москва'
    with pytest.raises(AttributeError):
        create_exemplar.filter_by_area(0)
    assert create_exemplar.filter_by_area('Вымышленный город') == []


def test_sort_to_salary_from(create_exemplar, path_for_tests_read):
    x = create_exemplar.sort_to_salary_from()
    assert x[-1]['salary']['from'] > x[-3]['salary']['from']
    x = x[::-1]
    assert x[0]['salary']['from'] > x[2]['salary']['from']
