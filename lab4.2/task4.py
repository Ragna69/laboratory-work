# import numpy as np
# from scipy import integrate
#
# # f(x) = sin(x^2)
# def f1(x):
#     return np.sin(x**2)
#
# # Вычисление интеграла от 0 до 2
# I1, _ = integrate.quad(f1, 0, 2)
#
# # --- Двойной интеграл ---
# # f(x, y) = x * y
# def f2(x, y):
#     return x * y
#
# # Пределы интегрирования: x от 0 до 2, y от 0 до 3
# I2, _ = integrate.dblquad(f2, 0, 2, lambda x: 0, lambda x: 3)
#
# # Вывод результатов
# print(f"Определённый интеграл ∫₀² sin(x²) dx = {I1:.4f}")
# print(f"Двойной интеграл ∬ x·y dxdy на [0,2]×[0,3] = {I2:.4f}")

import numpy as np
from scipy import integrate


# Определённый интеграл
def f1(x):
    return np.sin(x**2)
I1, _ = integrate.quad(f1, 0, 2)

# Двойной интеграл
def f2(x, y):
    return x * y
I2, _ = integrate.dblquad(f2, 0, 2, lambda x: 0, lambda x: 3)

# с округлением до 4 знаков после запятой
print(f"Определённый интеграл ∫₀² sin(x²) dx = {I1:.4f}")
print(f"Двойной интеграл ∬ x·y dxdy на [0,2]×[0,3] = {I2:.4f}")