#Задача 6. Удаление дубликатов без set()

word_list = input('Введите список символов:\n').strip().split()

unique = []
for word in word_list:
    if word not in unique:
        unique.append(word) # .appent() - добавляет элемент в конец списка
print('Список без повторяющихся символов:', *unique)