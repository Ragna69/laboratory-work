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



