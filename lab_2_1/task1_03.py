#Задача 3. Второе по величине число

digits = input('Введите числа:\n').split()

minimal = [float(digit) for digit in digits if digit.lstrip('-').replace('.', '', 1).isdigit()]

if len(minimal) < 2:
    print('Введите больше одного числа.')
else:
    min_2 = min(minimal)
    # Фильтруем числа, которые больше минимального
    more_than_the_second = [x for x in minimal if x > min_2]

    if more_than_the_second:
        second = min(more_than_the_second)
        print('Первое большее минимального:', second)
    else:
        print('Нет числа, большего минимального.')
