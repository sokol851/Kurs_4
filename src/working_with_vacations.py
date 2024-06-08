from src.api_service import WorkingHH


class Vacancies:
    """
    Класс для работы с вакансиями.

    Методы:
        create_vacancies(cls, data) - получает JSON список и формирует список экземпляров вакансий.
    """
    def __init__(self, name, salary_from, salary_to, currency, area, requirement, url):
        self.name = name
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}','{self.salary_from}','{self.salary_to}','{self.currency}',"
                f"'{self.area}','{self.requirement}', '{self.url}')")

    def __str__(self):
        return (f'Вакансия: {self.name}\n'
                f'Заработная плата: от {self.salary_from} до {self.salary_to} {self.currency}\n'
                f'Местоположение: {self.area}\n'
                f'Требования: {self.requirement}\n'
                f'Сcылка на ваканисию: {self.url}')

    @classmethod
    def create_vacancies(cls, data):
        vacancies = []
        for vac in data:
            name = vac.get('name')
            url = vac.get('alternate_url')
            area = vac.get('area').get('name')
            try:
                salary_from = vac.get('salary').get('from')
            except AttributeError:
                salary_from = 0
            try:
                salary_to = vac.get('salary').get('to')
            except AttributeError:
                salary_to = 0
            try:
                currency = vac.get('salary').get('currency')
            except AttributeError:
                currency = ''
            requirement = vac.get('snippet').get('requirement')
            vacancy = cls(name, salary_from, salary_to, currency, area, requirement, url)
            vacancies.append(vacancy)
        return vacancies
