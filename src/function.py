from src.working_with_vacations import Vacancies
from src.api_service import WorkingHH


def work_with_user():
    keyword = input('Введите запрос для поиска: ')
    if keyword == '':
        print('Вы не ввели запрос. Будут выведены любые вакансии.')
    number = input('Введите кол-во вакансий для поиска от 1 до 100: ')
    while not number.isdigit():
        print('Неверно выбрано количество вакансий. Могут быть только числа от 1 до 100.')
        number = input('Введите кол-во вакансий для поиска: ')
    if number == '':
        number = 1
    if int(number) > 100:
        number = 100
        print('Не может быть больше 100')
        input('Нажмите Enter, чтобы продолжить вывод 100 вакансий.')
    x = WorkingHH().load_vacancies(keyword, number)
    for i in Vacancies.create_vacancies(x):
        print(f'\n{i}')
