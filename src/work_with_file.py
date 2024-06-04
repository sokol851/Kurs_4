from abc import ABC, abstractmethod
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
        self.path = os.path.join('data', file_name)

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
            if i['url'] == url_vacancy:
                file_vacancy.remove(i)
                print(f'Вакансия: {i["name"]} удалена.')
        self.write_vacancy(file_vacancy)

    def clear_json(self):
        file_vacancy: list[dict] = []
        self.write_vacancy(file_vacancy)
