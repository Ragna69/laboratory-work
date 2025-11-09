import numpy as np

lengths_str = "63 13 9 18 -5 76 16 16 6 3"
speeds_str = "44 20 3462 346 42 52 38 1 66 67"
k = 3
p = 8

# Преобразование строк в массивы
lengths = np.fromstring(lengths_str, sep=' ')
speeds = np.fromstring(speeds_str, sep=' ')

segment_lengths = lengths[k-1:p]
segment_speeds = speeds[k-1:p]

S = np.sum(segment_lengths)

time = segment_lengths / segment_speeds
T = np.sum(time)

# Средняя скорость
V = S / T

print(f"S = {S:.0f} км, T = {T:.2f} час, V = {V:.2f} км/ч")
