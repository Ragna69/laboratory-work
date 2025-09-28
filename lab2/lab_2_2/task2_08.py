# 8) Замер времени
# Напишите декоратор @timing, который выводит на экран время выполнения функции в миллисекундах

import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time() # фиксирует время начала выполнения (в секундах)
#            ╭─ time.time() — текущее время в секундах
#            ╰─ start — момент запуска функции
        result = func(*args, **kwargs)  # вызывает оригинальную функцию с переданными аргументами
        end = time.time() # фиксируем время окончания выполнения
        duration_ms = (end - start) * 1000  # вычисляем длительность в миллисекундах

        print(f"Время выполнения: {duration_ms:.2f} мс")
        return result
    return wrapper

@timing
def slow_function():  # выполняет подсчёт суммы
    total = 0  # для накопления суммы
    for i in range(10**6): # цикл от 0 до 1000000
        total += i
    return total

result = slow_function()

