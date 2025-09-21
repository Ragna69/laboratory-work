a = input('Введите Фамилию:\n')
b = input('Введите Имя:\n')
c = input('Введите Отчество:\n')
if not a or not b or not c:
    print('Все поля должны быть заполнены')
result = a + ' ' + b[0] + '.' + c[0] + '.'
print(result)
