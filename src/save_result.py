from abc import ABC, abstractmethod
import json
from src.function import work_with_user


class FileWorking(ABC):
    @abstractmethod
    def file_working(self):
        pass


class SaveResult(FileWorking):
    def __init__(self):
        self.vac_list = work_with_user()

    def file_working(self):
        with open('./data/vacations.json', 'w', ) as file:
            json.dump(self, file, indent=4, ensure_ascii=False)
