import numpy as np

# Входные данные
lengths_str = "20 8 9 18 5 12 16 16 6 7"
speeds_str = "44 70 44 66 46 38 38 37 66 67"
k = 4
p = 7

# Преобразование строк в массивы
lengths = np.fromstring(lengths_str, sep=' ')
speeds = np.fromstring(speeds_str, sep=' ')

# Индексы участков: от k до p включительно → индексы k-1 до p
segment_lengths = lengths[k-1:p]
segment_speeds = speeds[k-1:p]

# Общая длина пути
S = np.sum(segment_lengths)

# Время на каждом участке: длина / скорость
times = segment_lengths / segment_speeds
T = np.sum(times)

# Средняя скорость: общая длина / общее время
V = S / T

# Вывод результатов
print(f"S = {S:.0f} км, T = {T:.2f} час, V = {V:.2f} км/ч")
