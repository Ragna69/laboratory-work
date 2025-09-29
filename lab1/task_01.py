# 1) ФИО

surname = input('Введите Фамилию:\n')
name = input('Введите Имя:\n')
otchestvo = input('Введите Отчество:\n')
if not surname or not name or not otchestvo:
    print('Все поля должны быть заполнены')
result = surname + ' ' + name[0] + '.' + otchestvo[0] + '.'
print(result)