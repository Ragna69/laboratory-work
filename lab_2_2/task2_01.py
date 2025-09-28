# 1) Модификация списка

# Напишите функцию, которая принимает список и делает его “плоским”.
# Используйте рекурсию. Функция должна модифицировать переданный список, а не создавать новый.
# Пример:
# >> list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
# >> flatten_list(list_a)
# >> print(list_a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

def list_modification(lst):
    i = 0
    while i < len(lst):               # продолжается, пока не дойдём до конца списка. while, потому что длинна может - и +
        if isinstance(lst[i], list):  # является ли текущий элемент вложенным списком
            list_modification(lst[i]) # рекурсия, чтобы развернуть вложенность внутри вложенного списка.
#                                  ╭─ lst[i] — вложенный список
            lst[i:i+1] = lst[i] # ─┼─ lst[i:i+1] — содержит сам вложенный список
#                                  ╰─ lst[i:i+1] = lst[i] — заменяет этот вложенный список на его содержимое
        else:
            i += 1

list_a = eval(input("Введите список (например: [1, 2, [3, [4]]]):\n")) # превращает строку в список (только с правильным вводом)
list_modification(list_a) # передает список в функцию
print("Плоский список:", list_a)

#для себя
# https://habr.com/ru/articles/560072/?ysclid=mg3s6w06ql879797145
# https://gitverse.ru/blog/articles/development/543-kak-ispolzovat-metod-eval-v-python
# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-eval/