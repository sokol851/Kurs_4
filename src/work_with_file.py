from abc import ABC, abstractmethod
from src.working_with_vacations import Vacancies
import json
import os
from config import ROOT_DIR


class FileWorking(ABC):
    @abstractmethod
    def read_vacancy(self):
        pass

    @abstractmethod
    def write_vacancy(self, data):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, url_vacancy):
        pass


class WorkWithJSON(FileWorking):

    def __init__(self, file_name: str):
        if not os.path.exists(f'{ROOT_DIR}/data'):
            os.mkdir(f'{ROOT_DIR}/data')
        self.path = os.path.join(ROOT_DIR, 'data', file_name)

    def read_vacancy(self):

        with open(self.path, 'r', encoding="utf8") as file:
            vac_list = json.load(file)
            return vac_list

    def write_vacancy(self, data):
        with open(self.path, 'w', encoding="utf8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        file_vacancy: list[dict] = self.read_vacancy()
        file_vacancy.append(vacancy)
        self.write_vacancy(file_vacancy)

    def del_vacancy(self, url_vacancy):
        file_vacancy: list[dict] = self.read_vacancy()
        for i in file_vacancy:
            if i['alternate_url'] == url_vacancy:
                file_vacancy.remove(i)
                print(f'Вакансия: {i["name"]} удалена.')
        self.write_vacancy(file_vacancy)

    def clear_json(self):
        file_vacancy: list[dict] = []
        self.write_vacancy(file_vacancy)

    @classmethod
    def filter_by_keyword(cls, keywords):
        vacancies = cls('vacancies.json')
        list_vacancies = vacancies.read_vacancy()
        vac_list_filter = []
        list_keyword = keywords.split(',')
        if list_vacancies is not None:
            for keyword in list_keyword:
                for i in list_vacancies:
                    if keyword.lower() in (i['name']).lower():
                        vac_list_filter.append(i)
                    if keyword.lower() in (i['snippet']['requirement']).lower():
                        vac_list_filter.append(i)
        for i in Vacancies.create_vacancies(vac_list_filter):
            print(f'\n{i}')
        print(f'\nНайдено по ключевым словам {len(vac_list_filter)} вакансий.')
        print(f'Записать результат?')
        input_user = input('Введите "да" или "нет": ')
        if input_user.lower() == 'да':
            vacancies.write_vacancy(vac_list_filter)

    @classmethod
    def filter_by_salary(cls, salary):
        vacancies = cls('vacancies.json')
        list_vacancies = vacancies.read_vacancy()
        vac_list_filter = []
        if int(salary) == 0:
            vac_list_filter = list_vacancies
        else:
            if list_vacancies is not None:
                for i in list_vacancies:
                    if i['salary'] is not None:
                        if i['salary']['from'] is not None:
                            if int(i['salary']['from']) >= int(salary):
                                vac_list_filter.append(i)
                        if i['salary']['to'] is not None:
                            if int(i['salary']['to']) >= int(salary):
                                vac_list_filter.append(i)
        for i in Vacancies.create_vacancies(vac_list_filter):
            print(f'\n{i}')
        print(f'\nНайдено по заработной плате {len(vac_list_filter)} вакансий.')
        print(f'Записать результат?')
        input_user = input('Введите "да" или "нет": ')
        if input_user.lower() == 'да':
            vacancies.write_vacancy(vac_list_filter)

    def sort_to_salary_from(self):
        vac_list = self.read_vacancy()
        sorted_vac_list = []
        for i in sorted(vac_list,
                        key=lambda x: x['salary']['from'] if x['salary'] and x['salary']['from'] is not None else 0,
                        reverse=False):
            sorted_vac_list.append(i)
        visual_vac_list = Vacancies.create_vacancies(sorted_vac_list)
        return [visual_vac_list, sorted_vac_list]
