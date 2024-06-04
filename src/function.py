from src.working_with_vacations import Vacancies
from src.api_service import WorkingHH


def work_with_user():
    vac_list = []
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
    x = WorkingHH().get_vacancies(keyword, number)
    for visual_vac in Vacancies.create_vacancies(x):
        print(f'\n{visual_vac}')
    for default_vac in WorkingHH().get_vacancies(keyword, number):
        vac_list.append(default_vac)
    return vac_list
