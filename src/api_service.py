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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.url_get}')"

    def load_vacancies(self, keyword):
        response = requests.get(self.url_get, params={'text': keyword, 'area': '113',
                                                      'per_page': input('Введите кол-во вакансий для поиска: ')})
        vacancies = response.json()['items']
        return vacancies


# if __name__ == '__main__':
#     x = WorkingHH()
#     print(x.load_vacancies('python')[0])
