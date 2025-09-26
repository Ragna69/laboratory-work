s = int(input('Введите целую сумму в рублях:'))
#if s % 1 != 0:
#    print('Это не целое число.')
#else:
a = s // 100
s = s - a * 100
b = s // 50
s = s - b * 50
c = s // 10
s = s - c * 10
d = s // 5
s = s - d * 5
e = s // 2
s = s - e * 2
f = s // 1
s = s - d * 1
result = (a, b, c, d, e, f)
print(result)
