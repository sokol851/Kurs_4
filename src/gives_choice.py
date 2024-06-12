from src.work_with_vacancies import Vacancies
from src.work_with_file import WorkWithJSON


def gives_choice():
    """
    Главное меню программы.
    Указав номер получаем необходимые действия с вакансиями:
            1. Поиск вакансий на HeadHunter.
            2. Добавить вакансию по URL.
            3. Удалить вакансию по URL.
            4. Просмотр сохранённого списка.
            5. Фильтр вакансий по ключевому слову.
            6. Фильтр вакансий по заработной плате.
            7. Фильтр вакансий по городу.
            8. Сортировка вакансий по заработной плате (По возрастанию).
            9. Сортировка вакансий по заработной плате (По убыванию).
            10. Очистка сохранённого списка.
            11. Завершить работу.
    """
    vacancies = WorkWithJSON('vacancies.json')
    list_vacancies = []
    vac = Vacancies('name', 'salary_from', 'salary_to', 'currency',
                    'area', 'requirement', 'url')
    print('Приветствую! Данное меню предназначено для работы с вакансиями на HeadHunter.ru')
    while True:
        print('\n1. Поиск вакансий на HeadHunter.\n'
              '2. Добавить вакансию по URL.\n'
              '3. Удалить вакансию по URL.\n'
              '4. Просмотр сохранённого списка.\n'
              '5. Фильтр вакансий по ключевому слову.\n'
              '6. Фильтр вакансий по заработной плате.\n'
              '7. Фильтр вакансий по городу.\n'
              '8. Сортировка вакансий по заработной плате (По возрастанию).\n'
              '9. Сортировка вакансий по заработной плате (По убыванию).\n'
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
            vacancies.ask_to_write(list_vacancies)
        if int(number) == 2:
            vacancies.add_vacancy(list_vacancies, input('Введите URL для сохранения (можно через запятую): '))
        if int(number) == 3:
            vacancies.del_vacancy(input('Введите URL для удаления (можно через запятую): '))
        if int(number) == 4:
            vac_list = vacancies.read_vacancy()
            vacancies.output_list_vac(vac_list)
        if int(number) == 5:
            vac_list_filter = vacancies.filter_by_keyword(input('Введите ключевые слова через запятую: '))
            vacancies.output_list_vac(vac_list_filter)
            vacancies.ask_to_write(vac_list_filter)
        if int(number) == 6:
            vac_list_filter = vacancies.filter_by_salary(input('Введите желаемую оплату: '))
            vacancies.output_list_vac(vac_list_filter)
            vacancies.ask_to_write(vac_list_filter)
        if int(number) == 7:
            vac_list_filter = vacancies.filter_by_area(input('Введите город: '))
            vacancies.output_list_vac(vac_list_filter)
            vacancies.ask_to_write(vac_list_filter)
        if int(number) == 8:
            vac_list = vacancies.sort_to_salary_from()
            vacancies.output_list_vac(vac_list)
            vacancies.ask_to_write(vac_list)
        if int(number) == 9:
            vac_list = vacancies.sort_to_salary_from()[::-1]
            vacancies.output_list_vac(vac_list)
            vacancies.ask_to_write(vac_list)
        if int(number) == 10:
            vacancies.clear_json()
        if int(number) == 11:
            return print('Работа завершена!')
