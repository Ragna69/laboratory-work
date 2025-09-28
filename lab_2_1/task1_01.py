#Задача 1. Посчитать слова

text = input('Введите текст:\n')
words  = text.lower().split()

spisok = {}
for word in words:
    spisok[word] = spisok.get(word, 0) + 1   # добавляет счетчик к слову
print('Список слов:')
for word in spisok:
    print(word, spisok[word])
unikalnie = len(spisok)
print('Количество уникальных слов:', str(unikalnie))



