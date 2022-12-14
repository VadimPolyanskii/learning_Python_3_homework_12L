# Задача: Используя HH API, рассчитать среднюю зарплату в Москве по запросу "Python".

import requests
import pprint

# Выясняем кол-во страниц с вакансиями Python
# URL = 'https://api.hh.ru/vacancies'
#
# par = {'text': 'Python',
#        'page':1}
# res = requests.get(URL, params=par).json()
# pprint.pprint(res)


x = []    # список вакансий

# Счётчики зп
all_zp = 0
all_n = 0

# Пройдём циклом по всем вакансиям Python (на 100 страницах)
for i in range(100):
    URL = 'https://api.hh.ru/vacancies'
    # Параметры запроса
    par = {'text': 'Python', 'parent_id': "113", 'name': "Москва", 'page': i}
    r = requests.get(URL, params=par)
    e = r.json()
    x.append(e)

# Пройдём циклом по списку вакансий
for j in x:
    y = j['items']
    # Объявляем переменную n для подсчета количества итераций цикла перебирающего зарплаты в вакансиях
    n = 0
    # Объявляем переменную sum_zp для подсчета суммы зарплат в вакансиях
    sum_zp = 0
    # Цикл, переберает объекты, т.е перебирает вакансии
    for i in y:
        # Проверяем есть ли значения в словаре по ключу salary, т.е проверяем есть ли в вакансии данные по зарплате
        if i['salary'] != None:
            # Записываем значение в переменную s
            s = i['salary']
            # Проверяем есть ли значения по ключу from, т.е проверяем есть ли в вакансии данные по минимальной зп
            if s['from'] != None:
                # Считаем количество обработанных вакансий в которых указана минимальная ЗП
                n += 1
                # Получаем минимальную ЗП по ключу from
                s['from']
                # Считаем сумму ЗП по вакансиям
                sum_zp += s['from']

    # Добавляем сумму зп по итерации цикла
    all_zp += sum_zp
    # Добавляем сумму n по итерации цикла
    all_n += n

# Считаем среднюю ЗП
av_zp = all_zp / all_n
print(av_zp)



