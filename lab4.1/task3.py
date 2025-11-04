# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(10, 10))
#
# from matplotlib.patches import Circle, Polygon, Rectangle
# fig, ax = plt.subplots()
# ax.circle(0, 0, 1, color='red')
# plt.title('Рисунок ...')
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

fig, ax = plt.subplots(figsize=(100, 100))

# Добавляем круг с центром (0, 0) и радиусом 1

#68 треугольников
color1  = (0.00, 0.00, 0.00)  # Чистый чёрный
color2  = (0.035, 0.035, 0.035)  # Очень тёмный
color3  = (0.07, 0.07, 0.07)  # Почти угольный
color4  = (0.105, 0.105, 0.105)  # Графитовый
color5  = (0.14, 0.14, 0.14)  # Абсолютный чёрный
color6  = (0.175, 0.175, 0.175)  # Тёмно-серый
color7  = (0.21, 0.21, 0.21)  # Серый с оттенком угля
color8  = (0.245, 0.245, 0.245)  # Серый
color9  = (0.28, 0.28, 0.28)  # Мягкий серый
color10 = (0.315, 0.315, 0.315)  # Теплый серый
color11 = (0.35, 0.35, 0.35)  # Светло-серый
color12 = (0.385, 0.385, 0.385)  # Почти светлый
color13 = (0.42, 0.42, 0.42)  # Серый с серебром
color14 = (0.455, 0.455, 0.455)  # Серебристый
color15 = (0.50, 0.50, 0.50)  # Средний серый
color16 = (0.9, 0.9, 0.9)  # Почти белый

#1
ax.add_patch(Polygon([[-9.6, 9.6], [-4, 6.4], [-5.8, 4.6]], closed=True, color=color6))
#2
ax.add_patch(Polygon([[-9.6, 9.6], [-8.4, 2.5], [-5.8, 4.6]], closed=True, color=color1))
#3
ax.add_patch(Polygon([[-4, 6.4], [0,6.4], [-5.8, 4.6]], closed=True, color=color4))
#4
ax.add_patch(Polygon([[-3, 4], [0,6.4], [-5.8, 4.6]], closed=True, color=color3))
#5
ax.add_patch(Polygon([[-3, 4], [-8.4, 2.5], [-5.8, 4.6]], closed=True, color=color1))
#6
ax.add_patch(Polygon([[-6.7, 2.3], [-8.4, 2.5], [-3, 4]], closed=True, color=color1))
#7
ax.add_patch(Polygon([[-3, 4], [0,6.4], [-1.2, 3]], closed=True, color=color2))
#8
ax.add_patch(Polygon([[0.8, 4.5], [0,6.4], [-1.2, 3]], closed=True, color=color3))
#9
ax.add_patch(Polygon([[0.8, 4.5], [3.1,5.5], [0,6.4]], closed=True, color=color2))
#10
ax.add_patch(Polygon([[2.8,6.8], [3.1,5.5], [0,6.4]], closed=True, color=color5))
#12
ax.add_patch(Polygon([[7.8, 9.6], [2.8,6.8], [3.1,5.5]], closed=True, color=color3))
#13
ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#14
ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#15
ax.add_patch(Polygon([[-6.7, 2.3], [-8.4, 2.5], [-9, -0.8]], closed=True, color=color1))
#16
ax.add_patch(Polygon([[-9, -0.8], [-6.7, 2.3], [-6.4, 0.5]], closed=True, color=color1))
#17
ax.add_patch(Polygon([[-4.2, 0.9], [-6.7, 2.3], [-6.4, 0.5]], closed=True, color=color3))
#18
ax.add_patch(Polygon([[-6.7, 2.3], [-4.2, 0.9], [-3, 4]], closed=True, color=color4))
#19
ax.add_patch(Polygon([[-9, -0.8], [-6.4, 0.5], [-5, -1.6]], closed=True, color=color4))
#20
ax.add_patch(Polygon([[-9, -0.8], [-8.4, -3.6], [-5, -1.6]], closed=True, color=color1))
#21
ax.add_patch(Polygon([[-4.8, -4.7], [-8.4, -3.6], [-5, -1.6]], closed=True, color=color1))
#22
ax.add_patch(Polygon([[-4.8, -4.7], [-8.4, -3.6], [-7, -5.6]], closed=True, color=color1))
#23
ax.add_patch(Polygon([[-4.8, -4.7], [-4.3, -6.4], [-7, -5.6]], closed=True, color=color2))
#24
ax.add_patch(Polygon([[-4.8, -4.7], [-4.3, -6.4], [-1.2, -5.2]], closed=True, color=color2))
#25
ax.add_patch(Polygon([[-4.8, -4.7], [-2.6, -3.6], [-1.2, -5.2]], closed=True, color=color4))
#26
ax.add_patch(Polygon([[-4.8, -4.7], [-2.6, -3.6], [-3, -0.8]], closed=True, color=color1))
#27
ax.add_patch(Polygon([[-4.8, -4.7], [-5, -1.6], [-3, -0.8]], closed=True, color=color2))
#28
ax.add_patch(Polygon([[-5, -0.1], [-6.4, 0.5], [-5, -1.6]], closed=True, color=color1))
#29
ax.add_patch(Polygon([[-5, -0.1], [-6.4, 0.5], [-4.2, 0.9]], closed=True, color=color1))
#30
ax.add_patch(Polygon([[-4, -0.4], [-5, -1.6], [-3, -0.8]], closed=True, color=color1))
#31
ax.add_patch(Polygon([[-4, -0.4], [-3, -0.8], [-4.2, 0.9]], closed=True, color=color2))
#32
#ax.add_patch(Polygon([[-4, -0.4], [-5, -0.1], [-4.2, 0.9]], closed=True, color=color16))
#33
#ax.add_patch(Polygon([[-4, -0.4], [-5, -0.1], [-5, -1.6]], closed=True, color=color16))
#34
ax.add_patch(Polygon([[-3, 4], [-3, -0.8], [-4.2, 0.9]], closed=True, color=color1))
#35
ax.add_patch(Polygon([[-3, 4], [-3, -0.8], [-1.2, 3]], closed=True, color=color3))
#36
ax.add_patch(Polygon([[-2.6, -3.6], [-3, -0.8], [-1.2, 3]], closed=True, color=color2))
#37
ax.add_patch(Polygon([[-2.6, -3.6], [-1.2, -1.1], [-1.2, 3]], closed=True, color=color1))
#38
ax.add_patch(Polygon([[0.2, -3.6], [-1.2, -1.1], [-1.2, 3]], closed=True, color=color2))
#39
ax.add_patch(Polygon([[0.2, -3.6], [-1.2, -1.1], [-2.6, -3.6]], closed=True, color=color4))
#40
ax.add_patch(Polygon([[0.2, -3.6], [-1.2, -5.2], [-2.6, -3.6]], closed=True, color=color1))
#41.
ax.add_patch(Polygon([[2.4, -4.7], [0.2, -3.6], [-1.2, -5.2]], closed=True, color=color4))
#42
ax.add_patch(Polygon([[2.4, -4.7], [2, -6.7], [-1.2, -5.2]], closed=True, color=color3))
#43
ax.add_patch(Polygon([[-1.1, -7.8], [2, -6.7], [-1.2, -5.2]], closed=True, color=color1))
#44
ax.add_patch(Polygon([[-1.1, -7.8], [-4.3, -6.4], [-1.2, -5.2]], closed=True, color=color1))
#45
ax.add_patch(Polygon([[2.4, -4.7], [0.2, -3.6], [0.7, -1.2]], closed=True, color=color2))
#46
ax.add_patch(Polygon([[-1.2, 3], [0.2, -3.6], [0.7, -1.2]], closed=True, color=color3))
#47

#48

#49
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#50
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#51
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#52
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#53
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#54
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#55
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#56
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#57
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#58
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#59
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#60
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#61
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#62
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#63
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#64
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#65
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#66
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#67
#ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#68



ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

plt.title('Рисунок кота')
plt.grid(False)
plt.show()