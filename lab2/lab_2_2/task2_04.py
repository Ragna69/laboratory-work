# 4) Транспонирование матрицы

# Пользователь вводит матрицу (список списков). Напишите функцию, которая транспонирует матрицу,
# не изменяя входную матрицу. Транспонирование матрицы - операция над матрицей,
# когда ее строки становятся столбцами с теми же номерами.

def transposition_of_the_matrix(matrix): # принимает матрицу и возвращает её транспонированную копию
    rows = len(matrix)  # количество строк
    columns = len(matrix[0]) # количество столбцов
    transposed = []  # пустой список

    for column in range(columns): # проходит по каждому столбцу
        new_row = []  # новая строка для транспонированной матрицы
        for row in range(rows): # проходит по каждой строке исходной матрицы
            new_row.append(matrix[row][column])# добавляет элемент из столбца в новую строку
#                    ╰────┬────╯ ╭ matrix[row][column] — берёт элемент из столбца column строки row
#                         ╰──────┴ new_row.append(...) — строкп транспонированной матрицы
        transposed.append(new_row) # добавляем сформированную строку в транспонированную матрицу
    return transposed

def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    print("Введите элементы матрицы по одному:")
    matrix = []
    for i in range(rows): # проходит по каждой строке
        current_row = []
        for j in range(cols):  # проходим по каждому столбцу
            value = int(input(f"Элемент [{i}][{j}]: "))
            current_row.append(value)
        matrix.append(current_row)

    return matrix

def print_matrix(matrix, title):
    print(f"\n{title}:") # выводим заголовок
    for row in matrix:
        print(" ".join(str(x) for x in row)) # выводим строку как последовательность чисел через пробел

original = input_matrix() # получает матрицу от пользователя
transposed = transposition_of_the_matrix(original) # транспонирует её

print_matrix(original, "Исходная матрица")
print_matrix(transposed, "Транспонированная матрица")
