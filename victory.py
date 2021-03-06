# Викторина "Угадай год рождения известных людей"

import random

# Словарь с датами рождения
# Имя и год рождения выбирается из словаря случайным образом N раз, могут быть повторения
data = {'А.С. Пушкина' : '26.05.1799', 'М.Ю. Лермонтова' : '03.10.1814', 'М.В. Ломоносова' : '08.11.1711',
        'Пётра I' : '30.05.1672', 'Екатерины Великой' : '02.05.1729', 'Николая II' : '18.05.1868',
        'Михаила Булгакова': '03.05.1891', 'Юрия Гагарина': '09.03.1934', 'Брэда Питта' : '18.12.1963',
        'Анджелины Джоли' : '04.06.1975', 'Джеймса Бонда (Шон Коннери)': '25.08.1930',
        'Терминатора (Арнольд Шварценеггер) ': '30.07.1947', 'Нео (Киану Ривз)': '02.09.1967',
        'Леонардо Ди Каприо': '11.11.1974', 'Джека Воробья (Джонни Депп)': '09.06.1963'}

day = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
       'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
       'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
       'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
       'двадцать девятое', 'тридцатое', 'тридцать первое']
month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

questions = 5; # количество вопросов

while True:
    # если пользователь ввёл 'да', будет выводиться подсказка даты рождения
    prompt = input('Если вам нужна подсказка, введите "да": ').lower() == 'да'

    print()
    correct_answer = 0; # количество правильных ответов

    for i in range(questions):
        key = ''.join(random.sample(list(data), 1))
        value = data[key]
        user_answer = input('Введите дату рождения ' + key + (' [' + value + ']' if prompt else '') + ': ')

        if (user_answer == value):
            print('Верно')
            correct_answer += 1
        else:
            date_split = value.split('.')
            day1 = date_split[0]
            day2 = day[int(date_split[0]) - 1]
            month1 = date_split[1]
            month2 = month[int(date_split[1]) - 1]
            print('Неверно, правильный ответ:', day[int(date_split[0]) - 1], month[int(date_split[1]) - 1], date_split[2], 'года')

        print()

    print('Викторина завершена')
    print()
    print('Правильных ответов:', correct_answer)
    print('Количество ошибок: ', questions - correct_answer)
    print()

    while True:
        answ = input('Повторить игру (да/нет)? ').lower()
        if answ == 'да' or answ == 'нет':
            break

    if answ == 'нет':
        break

    print()