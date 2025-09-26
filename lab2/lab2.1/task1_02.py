chisla = input('Введите числа:\n')
digits  = chisla.split()

spisok = {}
for digit in digits:
    spisok[digit] = spisok.get(digit, 0) + 1;

# print('Список слов:')
# for digit in spisok:
#     print(digit,':', spisok[digit])

unikalnie = len(spisok)
print('Количество уникальных чисел:', unikalnie)

print('Повторяющиеся числа:')
for digit in spisok:
    if spisok[digit] > 1:
        print(digit,':', spisok[digit])

