list_1 = input('Введите первый список чисел:\n').split()
list_2 = input('Введите второй список чисел:\n').split()

# преобразование строк в числа
digits_1 = [float(digit1) for digit1 in list_1 if digit1.lstrip('-').replace('.', '', 1).isdigit()]
digits_2 = [float(digit2) for digit2 in list_2 if digit2.lstrip('-').replace('.', '', 1).isdigit()]

#1
intersection = list(set(digits_1) & set(digits_2))
print('Числа, которые присутствуют в обоих наборах одновременно:')  # * - распаковывает список, чтобы числа выводились не в скобках
if intersection:
    print(*intersection, sep = ', ')
else:
    print('Таких чисел нет')

#2
first_is_second_no = list(set(digits_1) - set(digits_2))
print('Числа из первого набора, которые отсутствуют во втором:')
if first_is_second_no:
    print(*first_is_second_no, sep = ', ')
else:
    print('Таких чисел нет')


first_no_second_is = list(set(digits_2) - set(digits_1))
print('Числа из второго набора, которые отсутствуют во первом:')
if first_no_second_is:
    print(*first_no_second_is, sep = ', ')
else:
    print('Таких чисел нет')

#3
summa = list(set(digits_2) | set(digits_1))
both_minus_intersection = list(set(summa) - set(intersection))
print('Числа из обоих наборов, за исключением чисел, найденных в пункте 1:')
if both_minus_intersection:
    print(*both_minus_intersection, sep = ', ')
else:
    print('Таких чисел нет')