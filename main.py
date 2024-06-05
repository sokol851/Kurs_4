from src.work_with_file import WorkWithJSON
from src.working_with_vacations import Vacancies
from src.api_service import WorkingHH
from src.function import vacancies_output

# if __name__ == '__main__':
    # vacancies_output()
    # keyword = input('Введите запрос для поиска: ')
    # number = input('Введите кол-во вакансий для поиска: ')
    # hh = WorkingHH()
    # vacancies_dicts = hh.get_vacancies(keyword, number)
    # print(vacancies_dicts)
# #
#     y = WorkWithJSON('save_vacancies.json')
# # ######################################
# # # Чтение JSON
#     print(y.read_vacancy())
#     for vacancy in y.read_vacancy():
#         print_for_user = Vacancies(*vacancy.values())
#         print(f'\n{print_for_user}')
#
# #######################################
# # Запись в JSON
#     for i in Vacancies.create_vacancies(vacancies_dicts):
#         print(f'\n{i}')
#         y.add_vacancy(i.to_json())
# #######################################
# # Удаление из JSON
#     x = input('введите url для удаления: ')
#     y.del_vacancy(x)
# #######################################
# # Очистка списка вакансий JSON
#     y.clear_json()
