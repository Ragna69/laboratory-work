# Козерог 22 декабря — 19 января
# Водолей 20 января — 18 февраля
# Рыбы 19 февраля — 20 марта
# Овен 21 марта — 20 апреля
# Телец	21 апреля — 20 мая
# Близнецы	21 мая — 21 июня
# Рак 22 июня — 22 июля
# Лев 23 июля — 22 августа
# Дева 23 августа — 22 сентября
# Весы 23 сентября — 22 октября
# Скорпион 23 октября — 22 ноября
# Стрелец 23 ноября — 22 декабря

den = int(input('Введите день рождения:'))
if den < 0 or den > 31:
    print('Ошибка: неправильный день!')
    exit()
mes = int(input('Введите месяц рождения:'))
if mes < 0 or mes > 12:
    print('Ошибка: неправильный месяц!')
    exit()
else:
    if (mes == 12 and den >= 22) or (mes == 1 and den <= 19):
        print('Ваш знак зодиака Козерог')
    elif (mes == 1 and den >= 20) or (mes == 2 and den <= 18):
        print('Ваш знак зодиака Водолей')
    elif (mes == 2 and den >= 19) or (mes == 3 and den <= 20):
        print('Ваш знак зодиака Рыбы')
    elif (mes == 3 and den >= 21) or (mes == 4 and den <= 20):
        print('Ваш знак зодиака Овен')
    elif (mes == 4 and den >= 21) or (mes == 5 and den <= 20):
        print('Ваш знак зодиака Телец')
    elif (mes == 5 and den >= 21) or (mes == 6 and den <= 21):
        print('Ваш знак зодиака Близнецы')
    elif (mes == 6 and den >= 22) or (mes == 7 and den <= 22):
        print('Ваш знак зодиака Рак')
    elif (mes == 7 and den >= 23) or (mes == 8 and den <= 22):
        print('Ваш знак зодиака Лев')
    elif (mes == 8 and den >= 23) or (mes == 9 and den <= 22):
        print('Ваш знак зодиака Дева')
    elif (mes == 9 and den >= 23) or (mes == 10 and den <= 22):
        print('Ваш знак зодиака Весы')
    elif (mes == 10 and den >= 23) or (mes == 11 and den <= 22):
        print('Ваш знак зодиака Скорпион')
    elif (mes == 11 and den >= 23) or (mes == 12 and den <= 22):
        print('Ваш знак зодиака Стрелец')




