from src.working_with_vacations import Vacancies
from src.api_service import WorkingHH
from src.work_with_file import WorkWithJSON
import os
from config import ROOT_DIR


def gives_choice():
    path_save_vacancies = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
    vacancies = WorkWithJSON(path_save_vacancies)
    print('Приветствую! Данное меню предназначено для работы с вакансиями на HeadHunter.ru')
    while True:
        print('\n1. Поиск вакансий.\n'
              '2. Удалить вакансию по URL.\n'
              '3. Просмотр сохранённого списка.\n'
              '4. Фильтр вакансий по ключевому слову.\n'
              '5. Фильтр вакансий по заработной плате.\n'
              '6. Сортировка списка по заработной плате (По возрастанию).\n'
              '7. Сортировка списка по заработной плате (По убыванию).\n'
              '8. Очистка сохранённого списка.\n'
              '9. Завершить работу.')
        number = input('Выберите необходимое действие (цифра от 1 до 9):\n')
        number = number.strip(' ')
        while not number.isdigit() or int(number) not in range(1, 10):
            print('Вы ввели неверный номер! Повторите:')
            number = input('Выберите необходимое действие (цифра от 1 до 9):\n')
            number = number.strip(' ')
        if int(number) == 1:
            vacancies.clear_json()
            list_vacancies = vacancies_output()
            for i in list_vacancies:
                vacancies.add_vacancy(i)
        if int(number) == 2:
            vacancies.del_vacancy(input('Введите URL для удаления: '))
        if int(number) == 3:
            vac_list = vacancies.read_vacancy()
            visual_vac_list = Vacancies.create_vacancies(vac_list)
            for i in visual_vac_list:
                print(f'\n{i}')
        if int(number) == 4:
            vacancies.filter_by_keyword(input('Введите ключевые слова через запятую (первое,второе): '))
        if int(number) == 5:
            vacancies.filter_by_salary(input('Введите желаемую оплату: '))
        if int(number) == 6:
            for i in vacancies.sort_to_salary_from()[0]:
                print(f'\n{i}')
            print(f'Записать результат?')
            input_user = input('Введите "да" или "нет": ')
            if input_user.lower() == 'да':
                vacancies.write_vacancy(vacancies.sort_to_salary_from()[1])
        if int(number) == 7:
            for i in vacancies.sort_to_salary_from()[0][::-1]:
                print(f'\n{i}')
            print(f'Записать результат?')
            input_user = input('Введите "да" или "нет": ')
            if input_user.lower() == 'да':
                vacancies.write_vacancy(vacancies.sort_to_salary_from()[1][::-1])
        if int(number) == 8:
            vacancies.clear_json()
            print('Список очищен')
        if int(number) == 9:
            return print('Работа завершена!')


def vacancies_output():
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
