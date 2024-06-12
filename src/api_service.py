from abc import ABC, abstractmethod
import requests


class ApiService(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, number):
        pass


class WorkingHH(ApiService):
    """
    API Сервис от HeadHunter
    """
    keyword: str
    number: str

    def __init__(self):
        self.__url_get = 'https://api.hh.ru/vacancies'
        self.__header = {'User-Agent': 'HH-User-Agent'}

    def get_vacancies(self, keyword, number) -> list[dict]:
        """Получает список указанного кол-ва вакансий по ключевому слову"""
        response = requests.get(self.__url_get, params={'text': keyword, 'area': '113', 'per_page': number})
        result = response.json()['items']
        return result
