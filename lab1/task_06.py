#n = PV/RT
#R = 8.31
P = int(input('Введите давление газа:\n'))
V = int(input('Введите объем газа:\n'))
T = int(input('Введите температуру газа\n'))
R = 8.31
if not P or not V or not T or not R:
    print('Заполните все поля!')
else:
    n = float((P*V)/(R*T))
    print('Количество газа в молях:\n', n)