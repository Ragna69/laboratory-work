summa = int(input('Введите целую сумму в рублях:'))
hungred = summa // 100
summa -= hungred * 100
fifty = summa // 50
summa -= fifty * 50
ten = summa // 10
summa -= ten * 10
five = summa // 5
summa -= five * 5
two = summa // 2
summa -= two * 2
one = summa // 1
summa -= one * 1
result = (hungred, fifty, ten, five, two, one)
print(result)
