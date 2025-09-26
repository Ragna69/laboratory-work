chisla = input('Введите числа:\n')
digits  = chisla.split()

spisok = {}
for digit in digits:
    spisok[digit] = spisok.get(digit, 0) + 1;

unikalnie = len(spisok)
print('Количество уникальных чисел:\n', unikalnie)

print('Повторяющиеся числа:')
found = False
for digit in spisok:
    if spisok[digit] > 1:
        print(digit,':', spisok[digit])
        found = True
if not found:
    print('0')

print('Четные числа:')
found = False
for digit in spisok:
    if not '-' or not '.' in digit:
        if int(digit) % 2 == 0:
           print(digit)
           found = True
if not found:
    print('0')

print('Нечетные числа:')
found = False
for digit in spisok:
    if not '-' or not '.' in digit:
       if int(digit) % 2 == 1:
           print(digit)
           found = True
if not found:
    print('0')

print('Отрицательные числа:')
found = False
for digit in spisok:
    if '-' in digit:
        print(digit)
        found = True
if not found:
    print('0')

print('Числа с плавающей точкой:')
found = False
for digit in spisok:
    if '.' in digit or 'e' in digit.lower():
        print(digit)
        found = True
if not found:
    print('0')

print('Сумма всех чисел, кратных 5:')
found = False
summa = sum(int(digit) for digit in digits if digit.lstrip('-').isdigit() and int(digit) % 5 ==0)
if summa:
    print(summa)
    found = True
if not found:
    print('0')

largest = [float(digit) for digit in digits if digit.lstrip('-').replace('.','',1).isdigit()]
if largest:
    largest = max(largest)
    print('Самое большое число:\n', largest)
else:
    print('Нет таких чисел')


minimal = [float(digit) for digit in digits if digit.lstrip('-').replace('.','',1).isdigit()]
if minimal:
    smallest = min(minimal)
    print('Самое маленькое число:\n', smallest)
else:
    print('Нет таких чисел')



