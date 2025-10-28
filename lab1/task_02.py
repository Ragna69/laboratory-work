string = input('Введите строку:')
if not string:
    print('Пустая строка')
else:
        string = string.replace('a', '').replace('o', '').replace('i', '').replace('u', '').replace('e', '').replace('y', '')
        print("Результат:", string)