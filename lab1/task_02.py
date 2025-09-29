s = input('Введите строку:')
if not s:
    print('Пустая строка')
else:
        g = "aeiou" # Введите строку и удалите из нее все гласные (a, e, i, o, u), затем выведите результат.
        result = ""
        for char in s:
            if char not in g:
                result += char
        print("Результат:", result)