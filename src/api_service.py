from abc import ABC, abstractmethod
import requests


class ApiService(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass


class WorkingHH(ApiService):

    def __init__(self, url_get='https://api.hh.ru/vacancies'):
        self.url_get = url_get
        super().__init__(url_get)

    def load_vacancies(self, keyword):
        response = requests.get(self.url_get, params={'text': keyword, 'area': '113', 'per_page': 100})
        vacancies = response.json()['items']
        return vacancies
