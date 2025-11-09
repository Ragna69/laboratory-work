import matplotlib.pyplot as plt
import math

# Интервал в градусах
degrees = range(-360,360)
x_degrees = list(degrees)

# Перевод в радианы
x_interval = [math.radians(x) for x in x_degrees]

# Вычисление f(x) и h(x)
f_x = [math.exp(math.cos(x)) + math.log(math.cos(0.6 * x)**2 + 1) * math.sin(x)
    for x in x_interval]
h_x = [-math.log((math.cos(x) + math.sin(x))**2 + 2.5) + 10
    for x in x_interval]

# Построение графиков
plt.figure(figsize=(10, 6)) # dpi=100, facecolor='white'
plt.plot(x_degrees, f_x, label='f(x)', color = 'black')
plt.plot(x_degrees, h_x, label='h(x)', color = 'red')

plt.title('Графики функций f(x) и h(x) на промежутке от −360° до 360°')
plt.xlabel('Градусы,°')
plt.ylabel('Значение функции')
plt.grid(True) #включает сетку на графике
plt.legend() #Показывает легенду — подписи к линиям
plt.show() #Открывает окно графика и отображает всё, что было построено


