p = input('Введите пароль:')
if len(p)<16:
    print('Пароль слишком короткий')

else:
    if p.isalpha() or p.isdigit():
        print('Пароль слабый')
    else:
        print('Пароль хороший')
