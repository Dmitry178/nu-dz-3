split_char = ','
# split_char = input('Введите разделитель: ') # для пользовательских видов разделителей
str_list = input('Введите числа через разделитель \'' + split_char + '\': ')
lst = str_list.split(split_char)
print('Результат:', ', '.join(set(lst)))
