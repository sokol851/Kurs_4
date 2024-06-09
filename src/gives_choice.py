from src.work_with_vacancies import Vacancies
from src.work_with_file import WorkWithJSON


def gives_choice():
    """
    Главное меню программы.
    Указав номер получаем необходимые действия с вакансиями:
            1. Поиск вакансий.
            2. Добавить вакансию по URL.
            3. Удалить вакансию по URL.
            4. Просмотр сохранённого списка.
            5. Фильтр вакансий по ключевому слову.
            6. Фильтр вакансий по заработной плате.
            7. Сортировка списка по заработной плате (По возрастанию).
            8. Сортировка списка по заработной плате (По убыванию).
            9. Очистка сохранённого списка.
            10. Завершить работу.
    """
    vacancies = WorkWithJSON('vacancies.json')
    list_vacancies = []
    vac = Vacancies('name', 'salary_from', 'salary_to', 'currency',
                    'area', 'requirement', 'url')
    print('Приветствую! Данное меню предназначено для работы с вакансиями на HeadHunter.ru')
    while True:
        print('\n1. Поиск вакансий.\n'
              '2. Добавить вакансию по URL.\n'
              '3. Удалить вакансию по URL.\n'
              '4. Просмотр сохранённого списка.\n'
              '5. Фильтр вакансий по ключевому слову.\n'
              '6. Фильтр вакансий по заработной плате.\n'
              '7. Фильтр вакансия по городу.\n'
              '8. Сортировка списка по заработной плате (По возрастанию).\n'
              '9. Сортировка списка по заработной плате (По убыванию).\n'
              '10. Очистка сохранённого списка.\n'
              '11. Завершить работу.')
        number = input('Выберите необходимое действие (цифра от 1 до 11):\n')
        number = number.strip(' ')
        while not number.isdigit() or int(number) not in range(1, 12):
            print('Вы ввели неверный номер! Повторите:')
            number = input('Выберите необходимое действие (цифра от 1 до 11):\n')
            number = number.strip(' ')
        if int(number) == 1:
            list_vacancies = vac.vacancies_output()
            print(f'Записать все результаты?')
            input_user = input('Введите "да" или "нет": ')
            if input_user.lower() == 'да':
                vacancies.write_vacancy(list_vacancies)
        if int(number) == 2:
            vacancies.add_vacancy(list_vacancies, input('Введите URL для сохранения (можно через запятую): '))
        if int(number) == 3:
            vacancies.del_vacancy(input('Введите URL для удаления (можно через запятую): '))
        if int(number) == 4:
            vac_list = vacancies.read_vacancy()
            visual_vac_list = vac.create_vacancies(vac_list)
            for i in visual_vac_list:
                print(f'\n{i}')
            print(f'\nВ списке {len(vac_list)} вакансий.')
        if int(number) == 5:
            vacancies.filter_by_keyword(input('Введите ключевые слова через запятую: '))
        if int(number) == 6:
            vacancies.filter_by_salary(input('Введите желаемую оплату: '))
        if int(number) == 7:
            vacancies.filter_by_area(input('Введите город: '))
        if int(number) == 8:
            for i in vacancies.sort_to_salary_from()[0]:
                print(f'\n{i}')
            print(f'Записать результат?')
            input_user = input('Введите "да" или "нет": ')
            if input_user.lower() == 'да':
                vacancies.write_vacancy(vacancies.sort_to_salary_from()[1])
        if int(number) == 9:
            for i in vacancies.sort_to_salary_from()[0][::-1]:
                print(f'\n{i}')
            print(f'Записать результат?')
            input_user = input('Введите "да" или "нет": ')
            if input_user.lower() == 'да':
                vacancies.write_vacancy(vacancies.sort_to_salary_from()[1][::-1])
        if int(number) == 10:
            vacancies.clear_json()
            print('Список очищен')
        if int(number) == 11:
            return print('Работа завершена!')
