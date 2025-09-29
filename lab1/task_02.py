string = input('Введите строку:')
if not string:
    print('Пустая строка')
else:
        symbols = "aeiou" # Введите строку и удалите из нее все гласные (a, e, i, o, u), затем выведите результат.
        result = "".join(symbol for symbol in string if symbol not in symbols)
        print("Результат:", result)