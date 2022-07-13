list1 = input('Введите элементы 1-го списка через запятую: ').split(',')
list2 = input('Введите элементы 2-го списка через запятую: ').split(',')

for val in range(len(list2)):
    while list2[val] in list1:
        list1.remove(list2[val])

print('Результат:', ', '.join(list1))