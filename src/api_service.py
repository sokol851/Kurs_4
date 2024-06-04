from abc import ABC, abstractmethod
import requests


class ApiService(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, number):
        pass


class WorkingHH(ApiService):

    def __init__(self):
        self.url_get = 'https://api.hh.ru/vacancies'
        self.header = {'User-Agent': 'HH-User-Agent'}

    def get_vacancies(self, keyword, number):
        response = requests.get(self.url_get, params={'text': keyword, 'area': '113', 'per_page': number})
        result = response.json()['items']
        return result


# if __name__ == '__main__':
#     x = WorkingHH()
#     print(x.load_vacancies('python')[0])
