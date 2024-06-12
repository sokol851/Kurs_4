def filter_by_keyword(data, keywords: str) -> [list[dict]]:
    """ Получает список слов, фильтрует JSON, выводит список фильтра. """
    list_vacancies = data.read_vacancy()
    vac_list_filter = []
    list_keyword = keywords.replace(' ', '').lower().split(',')
    if list_vacancies is not None:
        for i in list_vacancies:
            for keyword in list_keyword:
                if i['snippet']['requirement'] is not None:
                    if keyword in (i['name']).lower() or keyword in (i['snippet']['requirement']).lower():
                        if i not in vac_list_filter:
                            vac_list_filter.append(i)
    return vac_list_filter


def filter_by_salary(data, salary: str) -> [list[dict]]:
    """ Получает желаемую сумму, фильтрует JSON, выводит список фильтра. """
    list_vacancies = data.read_vacancy()
    vac_list_filter = []
    if not salary.isdigit():
        while not salary.isdigit():
            print(f'Неверно указана оплата!')
            salary = input('Введите оплату в цифрах:')
    if int(salary) == 0:
        vac_list_filter = list_vacancies
    else:
        if list_vacancies is not None:
            for i in list_vacancies:
                if i['salary'] is not None:
                    if i['salary']['from'] is not None:
                        if int(i['salary']['from']) >= int(salary):
                            if i not in vac_list_filter:
                                vac_list_filter.append(i)
                    if i['salary']['to'] is not None:
                        if int(i['salary']['to']) >= int(salary):
                            if i not in vac_list_filter:
                                vac_list_filter.append(i)
    return vac_list_filter


def filter_by_area(data, area: str) -> [list[dict]]:
    """ Получает город, фильтрует JSON, выводит список фильтра. """
    list_vacancies = data.read_vacancy()
    vac_list_filter = []
    area = area.replace(' ', '').lower()
    if list_vacancies is not None:
        for vac in list_vacancies:
            if area in (vac['area']['name']).lower():
                if vac not in vac_list_filter:
                    vac_list_filter.append(vac)
    return vac_list_filter


def sort_to_salary_from(data) -> list[dict]:
    """ Сортирует список по оплате от и до. Выводит  """
    vac_list = data.read_vacancy()
    sorted_vac_list = []
    for i in sorted(vac_list,
                    key=lambda x: x['salary']['from'] if x['salary'] and x['salary']['from'] is not None else 0,
                    reverse=False):
        sorted_vac_list.append(i)
    return sorted_vac_list
