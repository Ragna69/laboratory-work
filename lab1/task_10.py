a = input('Введите число а:\n')
if not a or not a.isdigit():
    print('Ошибка: пустая строка или не число')
else:
    b = input('Введите число b:\n')
    if not b or not b.isdigit():
        print('Ошибка: пустая строка или не число')
    else:
        summa = int(a)+int(b)
        print (summa)
        raznost = int(a)-int(b)
        print (raznost)
        chastnoe = int(a)//int(b)
        print (chastnoe)
        ostatok = int(a)%int(b)
        print (ostatok)
        stepen = int(a)**int(b)
        print (stepen)
