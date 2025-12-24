import matplotlib.pyplot as plt
import math

x_range = [x * 0.01 for x in range(-1000, 1000) ] #if x != 3 and x != -3

f_x = [5 / (x**2 - 9) if (x**2 - 9) != 0
       else math.nan #math.nan - не число, нужно для разрывов
    for x in x_range]

plt.figure(figsize=(10, 10))
plt.plot(x_range, f_x, color='black', label='f(x) = 5 / (x² - 9)')

# вертикальные асимптоты
plt.axvline(x=3, color='gray', linestyle='--')
plt.axvline(x=-3, color='gray', linestyle='--')

# горизонтальная асимптота
plt.axhline(y=0, color='black', linestyle=':')

plt.title('График функции f(x) = 5 / (x² - 9)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
