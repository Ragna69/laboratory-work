# #Задача 7. Сжатие строки

#1 способ
word_list = input('Введите список символов:\n')
if not word_list:
    print('Пустая строка.')
else:
    compressed = ''
    count = 1
    for i in range(1, len(word_list)):
        if word_list[i] == word_list[i-1]:  # если элемент равен предыдущему
            count += 1
        else:
            compressed += word_list[i-1] + str(count) # если не равен предыдущему, то добавляем в список
            count = 1
    compressed += word_list[-1] + str(count)
    print(compressed)


# 2 способ (он лучше, потому что учитывает повторяющиеся символы в независимости от расположения)
# from collections import Counter
# word_list = input('Введите список символов:\n').strip().split()
# #                           ┌─ from collections import Counter
# counts = Counter(word_list)#┼─ counts = Counter('aaabbc')
# #                           └─ {'a': 3, 'b': 2, 'c': 1}                  ┌─ ''.join() - склеивает элементы с разделителем м/ду ними.
# compressed = ''.join(f'{char}{count}' for char, count in counts.items())#┼─ f'{char}{count}' - вызывает значения переменных char и count.
# #                                                                        └─ count.items() - это метод словаря dict, который возвращает все пары ключ–значение.
# print(compressed)
