from src.api_service import WorkingHH


class Vacancies:
    """
    Класс для работы с вакансиями.
    """
    name: str
    salary_from: str
    salary_to: str
    currency: str
    area: str
    requirement: str
    url: str

    def __init__(self, name, salary_from, salary_to, currency, area, requirement, url):
        self.__name = name
        self.__area = area
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__currency = currency
        self.__url = url
        self.__requirement = requirement

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__name}','{self.__salary_from}','{self.__salary_to}',"
                f"'{self.__currency}','{self.__area}','{self.__requirement}','{self.__url}')")

    def __str__(self):
        return (f'Вакансия: {self.__name}\n'
                f'Заработная плата: от {self.__salary_from} до {self.__salary_to} {self.__currency}\n'
                f'Местоположение: {self.__area}\n'
                f'Требования: {self.__requirement}\n'
                f'Сcылка на вакансию: {self.__url}')

    def to_json(self) -> "Vacancies":
        """ Формирует экземпляр вакансии. """
        return Vacancies(self.__name, self.__salary_from, self.__salary_to, self.__currency, self.__area,
                         self.__requirement, self.__url)

    def create_vacancies(self, data) -> [list["Vacancies"]]:
        """ Получает JSON список и формирует список экземпляров вакансий. """
        vacancies = []
        for vac in data:
            self.__name = vac.get('name')
            self.__url = vac.get('alternate_url')
            self.__area = vac.get('area').get('name')
            try:
                if vac.get('salary').get('from') is None:
                    self.__salary_from = 0
                else:
                    self.__salary_from = vac.get('salary').get('from')
            except AttributeError:
                self.__salary_from = 0
            try:
                if vac.get('salary').get('to') is None:
                    self.__salary_to = 0
                else:
                    self.__salary_to = vac.get('salary').get('to')
            except AttributeError:
                self.__salary_to = 0
            try:
                self.__currency = vac.get('salary').get('currency')
            except AttributeError:
                self.__currency = ''
            if vac.get('snippet').get('requirement') is None:
                self.__requirement = 'Не указано.'
            else:
                self.__requirement = ((vac.get('snippet').get('requirement')).replace('<highlighttext>', '<')
                                      .replace('</highlighttext>', '>'))
            vacancy = self.to_json()
            vacancies.append(vacancy)
        return vacancies

    @staticmethod
    def vacancies_output() -> list[dict]:
        """ Формирует запрос для API с проверками ввода данных и выводит список готовых вакансий. """
        vac_list = []
        keyword = input('Введите запрос для поиска: ')
        if keyword == '':
            print('Вы не ввели запрос. Будут выведены любые вакансии.')
        number = input('Введите кол-во вакансий для поиска от 1 до 100: ')
        while not number.isdigit():
            print('Неверно выбрано количество вакансий. Могут быть только числа от 1 до 100.')
            number = input('Введите кол-во вакансий для поиска: ')
        if int(number) > 100:
            number = 100
            print('Не может быть больше 100')
            input('Нажмите Enter, чтобы продолжить вывод 100 вакансий.')
        for default_vac in WorkingHH().get_vacancies(keyword, number):
            vac_list.append(default_vac)
        return vac_list
