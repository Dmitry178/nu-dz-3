while True:
    try:
        num = int(input('Введите количество элементов: '))
        if num < 0:
            raise Exception()
    except:
        print('Неверное значение')
    else:
        break

print()
lst = []

for i in range(num):
    while True:
        try:
            element = int(input('Введите ' + str(i) + ' элемент: '))
        except:
            print('Неверное значение')
        else:
            break

    lst.append(element)

print()
lst.sort()
print('Вывод:', lst)