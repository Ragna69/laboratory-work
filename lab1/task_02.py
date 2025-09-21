s = input('Введите строку:')
if not s:
    print('Пустая строка')
else:
        g = "aeiouAEIOUуеыаоэяию"
        result = ""
        for char in s:
            if char not in g:
                result += char
        print("Результат:", result)