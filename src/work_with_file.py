from abc import ABC, abstractmethod
from src.working_with_vacations import Vacancies
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
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, url_vacancy):
        pass


class WorkWithJSON(FileWorking):
    def __init__(self, file_name: str):
        self.path = os.path.join('../data', file_name)

    def read_vacancy(self):
        with open(self.path, 'r', ) as file:
            vac_list = json.load(file)
            return vac_list

    def write_vacancy(self, data):
        with open(self.path, 'w', ) as file:
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
        save_vacancies = cls('save_vacancies.json')
        list_vacancies = save_vacancies.read_vacancy()
        vac_list_filter = []
        list_keyword = keywords.split(',')
        print(list_keyword)
        if list_vacancies is not None:
            for keyword in list_keyword:
                for i in list_vacancies:
                    if keyword.lower() in (i['name']).lower():
                        vac_list_filter.append(i)
                    if keyword.lower() in (i['snippet']['requirement']).lower():
                        vac_list_filter.append(i)
        for i in Vacancies.create_vacancies(vac_list_filter):
            print(f'\n{i}')
        print(f'\nЗаписать результат?')
        input_user = input('Введите "да" или "нет": ')
        if input_user.lower() == 'да':
            save_vacancies.write_vacancy(vac_list_filter)

