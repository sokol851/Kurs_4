from src.working_with_vacations import Vacancies
from src.api_service import WorkingHH
from src.work_with_file import WorkWithJSON
import os


def gives_choice():
    path_vacancies = os.path.abspath('../data/vacancies.json')
    path_save_vacancies = os.path.abspath('../data/save_vacancies.json')
    vacancies = WorkWithJSON(path_vacancies)
    save_vacancies = WorkWithJSON(path_save_vacancies)
    print('Приветствую!')
    while True:
        print('\n1. Поиск вакансий.\n'
              '2. Запись найденых вакансий в список.\n'
              '3. Удалить вакансию по URL\n'
              '4. Просмотр сохранённого списка.\n'
              '5. Фильтр вакансий по ключевому слову.\n'
              '6. Сортировка списка по зар. плате. (По убыванию)\n'
              '7. Сортировка списка по зар. плате. (По возрастанию)\n'
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
            x = vacancies.read_vacancy()
            for i in x:
                save_vacancies.add_vacancy(i)
            # list_vacancies = []
            # for k in Vacancies.create_vacancies(vacancies.read_vacancy()):
            #     list_vacancies.append(Vacancies.to_json(k))
            # save_vacancies.add_vacancy(list_vacancies)
        if int(number) == 3:
            save_vacancies.del_vacancy(input('Введите URL для удаления: '))
        if int(number) == 4:
            vac_list = save_vacancies.read_vacancy()
            visual_vac_list = Vacancies.create_vacancies(vac_list)
            for i in visual_vac_list:
                print(f'\n{i}')
        if int(number) == 5:
            save_vacancies.filter_by_keyword(input('Введите ключевые слова через запятую (первое,второе):'))
        # if int(number) == 6:
            # sorted(save_vacancies.read_vacancy(), key=lambda x: x.salary_from)
        # if int(number) == 7:
            # sorted(save_vacancies.read_vacancy(), key=lambda x: x.salary_from)
        if int(number) == 8:
            save_vacancies.clear_json()
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


if __name__ == '__main__':
    gives_choice()
