num = int(input('Введите число:'))
if num%7 == 0:
    print('Магическое число!')
else:
    summa = sum(int(digit) for digit in str(num) if digit.isdigit())
    print('Сумма цифр:', summa)


