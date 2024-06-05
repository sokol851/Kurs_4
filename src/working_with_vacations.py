from src.api_service import WorkingHH


class Vacancies:

    def __init__(self, name, salary_from, salary_to, currency, area, requirement, url):
        self.name = name
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url
        self.requirement = requirement
        self.validate()

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}','{self.salary_from}','{self.salary_to}','{self.currency}',"
                f"'{self.area}','{self.requirement}', '{self.url}')")

    def __str__(self):
        return (f'Вакансия: {self.name}\n'
                f'Заработная плата: от {self.salary_from} до {self.salary_to} {self.currency}\n'
                f'Местоположение: {self.area}\n'
                f'Требования: {self.requirement}\n'
                f'Сcылка на ваканисию: {self.url}')

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def validate(self):
        if self.area is None:
            self.area = 'Не указано'
        if self.salary_from is None:
            self.salary_from = 0
        if self.salary_to is None:
            self.salary_to = 0
        if self.currency is None:
            self.currency = ''
        if self.requirement is None:
            self.requirement = 'Не указано'

    def to_json(self):
        return {'name': self.name,
                'salary_from': self.salary_from,
                'salary_to': self.salary_to,
                'currency': self.currency,
                'area': self.area,
                'requirement': self.requirement,
                'url': self.url}

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


# if __name__ == '__main__':
#     keyword = input('Введите запрос для поиска: ')
#     number = input('Введите кол-во вакансий для поиска: ')
#     if number == '':
#         number = 1
#     if int(number) > 100:
#         number = 100
#         print('Не может быть больше 100')
#         input('Нажмите Enter, чтобы продолжить вывод 100 вакансий.')
#     x = WorkingHH().get_vacancies(keyword, number)
#     print(Vacancies.create_vacancies(x)[0].name)
#     print(Vacancies.create_vacancies(x)[0].url)
#     print(Vacancies.create_vacancies(x)[0].area)
#     print(Vacancies.create_vacancies(x)[0].salary_from)
#     print(Vacancies.create_vacancies(x)[0].salary_to)
#     print(Vacancies.create_vacancies(x)[0].currency)
#     print(Vacancies.create_vacancies(x)[0].requirement)
#
#     for i in Vacancies.create_vacancies(x):
#         print(f'\n{i}')
