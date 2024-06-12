from src.work_with_vacancies import Vacancies
from abc import ABC, abstractmethod
from config import ROOT_DIR
import json
import os


class FileWorking(ABC):
    @abstractmethod
    def read_vacancy(self):
        pass

    @abstractmethod
    def write_vacancy(self, data):
        pass

    @abstractmethod
    def add_vacancy(self, list_vacancies, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, url_vacancy):
        pass


class WorkWithJSON(FileWorking):
    """
    Класс для работы с JSON.
    """
    file_name: str

    def __init__(self, file_name: str):
        """ При инициализации создаёт json файл и папку data в корне программы. """
        if file_name != 'test_vacancies.json':
            if not os.path.exists(f'{ROOT_DIR}/data'):
                os.mkdir(f'{ROOT_DIR}/data')
                self._path = os.path.join(ROOT_DIR, 'data', file_name)
                self.write_vacancy([])
            elif not os.path.exists(f'{ROOT_DIR}/data/{file_name}'):
                open(f'{ROOT_DIR}/data/{file_name}', 'w', encoding="utf8").close()
                self._path = os.path.join(ROOT_DIR, 'data', file_name)
                self.write_vacancy([])
            else:
                self._path = os.path.join(ROOT_DIR, 'data', file_name)
        self.__vac = Vacancies('name', 'salary_from', 'salary_to', 'currency',
                               'area', 'requirement', 'url')

    def read_vacancy(self) -> list[dict]:
        """ Читает список json конвертируя его в список. """
        with open(self._path, 'r', encoding="utf8") as file:
            vac_list = json.load(file)
            return vac_list

    def write_vacancy(self, data: list[dict]) -> None:
        """ Получает список вакансий, конвертирует и записывает JSON. """
        with open(self._path, 'w', encoding="utf8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, list_vacancies: list[dict], url_vacancy: str) -> None:
        """ Получает вакансии и url и добавляет вакансию по URL в JSON. """
        save_list_vacancies: list[dict] = self.read_vacancy()
        list_url = url_vacancy.replace(' ', '').lower().split(',')
        for url in list_url:
            for vac in list_vacancies:
                if vac['alternate_url'] == url:
                    if vac not in save_list_vacancies:
                        save_list_vacancies.append(vac)
                        print(f'Вакансия: {vac["name"]} добавлена.')
                    else:
                        print(f'Вакансия: {vac['name']} уже в списке.')
        self.write_vacancy(save_list_vacancies)

    def del_vacancy(self, url_vacancy: str) -> None:
        """ Получает url и удаляет вакансию по URL из JSON. """
        file_vacancy: list[dict] = self.read_vacancy()
        list_url = url_vacancy.replace(' ', '').lower().split(',')
        for url in list_url:
            for i in file_vacancy:
                if i['alternate_url'] == url:
                    file_vacancy.remove(i)
                    print(f'Вакансия: {i["name"]} удалена.')
        self.write_vacancy(file_vacancy)

    def clear_json(self) -> None:
        """ Очищает список. """
        file_vacancy: list[dict] = []
        print('Список очищен')
        self.write_vacancy(file_vacancy)

    def output_list_vac(self, vac_list_filter):
        for i in self.__vac.create_vacancies(vac_list_filter):
            print(f'\n{i}')
        print(f'\nНайдено {len(vac_list_filter)} вакансий.')

    def ask_to_write(self, data) -> None:
        """ Получает список вакансий и спрашивает записать ли результат в JSON. """
        print(f'Записать результат?')
        input_user = input('Введите "да" или "нет": ')
        if input_user.lower() == 'да':
            self.write_vacancy(data)

    def filter_by_keyword(self, keywords: str) -> [list[dict]]:
        """ Получает список слов, фильтрует JSON, выводит список фильтра. """
        list_vacancies = self.read_vacancy()
        vac_list_filter = []
        list_keyword = keywords.replace(' ', '').lower().split(',')
        if list_vacancies is not None:
            for i in list_vacancies:
                for keyword in list_keyword:
                    if i['snippet']['requirement'] is not None:
                        if keyword in (i['name']).lower() or keyword in (i['snippet']['requirement']).lower():
                            if i not in vac_list_filter:
                                vac_list_filter.append(i)
        return vac_list_filter

    def filter_by_salary(self, salary: str) -> [list[dict]]:
        """ Получает желаемую сумму, фильтрует JSON, выводит список фильтра. """
        list_vacancies = self.read_vacancy()
        vac_list_filter = []
        if not salary.isdigit():
            while not salary.isdigit():
                print(f'Неверно указана оплата!')
                salary = input('Введите оплату в цифрах:')
        if int(salary) == 0:
            vac_list_filter = list_vacancies
        else:
            if list_vacancies is not None:
                for i in list_vacancies:
                    if i['salary'] is not None:
                        if i['salary']['from'] is not None:
                            if int(i['salary']['from']) >= int(salary):
                                if i not in vac_list_filter:
                                    vac_list_filter.append(i)
                        if i['salary']['to'] is not None:
                            if int(i['salary']['to']) >= int(salary):
                                if i not in vac_list_filter:
                                    vac_list_filter.append(i)
        return vac_list_filter

    def filter_by_area(self, area: str) -> [list[dict]]:
        """ Получает город, фильтрует JSON, выводит список фильтра. """
        list_vacancies = self.read_vacancy()
        vac_list_filter = []
        area = area.replace(' ', '').lower()
        if list_vacancies is not None:
            for vac in list_vacancies:
                if area in (vac['area']['name']).lower():
                    if vac not in vac_list_filter:
                        vac_list_filter.append(vac)
        return vac_list_filter

    def sort_to_salary_from(self) -> list[dict]:
        """ Сортирует список по оплате от и до. Выводит  """
        vac_list = self.read_vacancy()
        sorted_vac_list = []
        for i in sorted(vac_list,
                        key=lambda x: x['salary']['from'] if x['salary'] and x['salary']['from'] is not None else 0,
                        reverse=False):
            sorted_vac_list.append(i)
        return sorted_vac_list
