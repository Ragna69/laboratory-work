import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle

fig, ax = plt.subplots(figsize=(100, 100))

ax.set_xlim(-10, 8.2)
ax.set_ylim(-7.9, 10)

# Для кота
color1  = (0.00, 0.00, 0.00)  # Чистый чёрный
color2  = (0.035, 0.035, 0.035)  # Очень тёмный
color3  = (0.07, 0.07, 0.07)  # Почти угольный
color4  = (0.105, 0.105, 0.105)  # Графитовый
color5  = (0.14, 0.14, 0.14)  # Абсолютный чёрный

violet1 = (0.1, 0.05, 0.2, 1.0)   # Тёмно-фиолетовый (почти чёрный)
violet2 = (0.2, 0.1, 0.4, 1.0)    # Глубокий индиго-фиолетовый
violet3 = (0.3, 0.15, 0.6, 1.0)   # Холодный фиолетовый
violet4 = (0.4, 0.2, 0.7, 1.0)    # Классический фиолетовый
violet5 = (0.5, 0.3, 0.8, 1.0)    # Яркий фиолетовый
violet6 = (0.6, 0.4, 0.9, 1.0)    # Светло-фиолетовый
violet7 = (0.7, 0.5, 1.0, 1.0)    # Сиреневый

# Для фона
violet8 = (0.3, 0.15, 0.6, 0.6)    # Светлый холодный фиолетовый
violet9 = (0.3, 0.15, 0.6, 0.5)   # Светлый холодный фиолетовый
violet10 = (0.4, 0.2, 0.7, 0.5)    # Светлый классический фиолетовый
violet11 = (0.5, 0.3, 0.8, 0.5)    # Светлый яркий фиолетовый
violet12 = (0.6, 0.4, 0.9, 0.5)    # Светлый светло-фиолетовый
violet13 = (0.7, 0.5, 1.0, 0.5)    # Светло-сиреневый
violet14 = (0.7, 0.5, 1.0, 0.6)    # Светло-сиреневый

# Фон
#1
ax.add_patch(Polygon([[-10, 10], [-10, 3], [-5.8, 10]], closed=True, color=violet11))
ax.add_patch(Polygon([[-10, 10], [-10, 3], [-5.8, 10]], closed=True, color=violet11))
ax.add_patch(Polygon([[-10, 10], [-10, 3], [-5.8, 10]], closed=True, color=violet12))
#2
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-5.8, 10]], closed=True, color=violet12))
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-5.8, 10]], closed=True, color=violet12))
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-5.8, 10]], closed=True, color=violet11))
#3
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-10, -3]], closed=True, color=violet10))
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-10, -3]], closed=True, color=violet10))
ax.add_patch(Polygon([[-5, -1], [-10, 3], [-10, -3]], closed=True, color=violet10))
#4
ax.add_patch(Polygon([[-10, -7.9], [-2, -7.9], [-10, -3]], closed=True, color=violet8))
ax.add_patch(Polygon([[-10, -7.9], [-2, -7.9], [-10, -3]], closed=True, color=violet8))
ax.add_patch(Polygon([[-10, -7.9], [-2, -7.9], [-10, -3]], closed=True, color=violet8))
#5
ax.add_patch(Polygon([[-5, -1], [-2, -7.9], [-10, -3]], closed=True, color=violet8))
ax.add_patch(Polygon([[-5, -1], [-2, -7.9], [-10, -3]], closed=True, color=violet9))
ax.add_patch(Polygon([[-5, -1], [-2, -7.9], [-10, -3]], closed=True, color=violet9))
#6
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [-5, -1]], closed=True, color=violet9))
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [-5, -1]], closed=True, color=violet9))
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [-5, -1]], closed=True, color=violet10))
#7
ax.add_patch(Polygon([[-5.8, 10], [-5, -1], [4, 2]], closed=True, color=violet11))
ax.add_patch(Polygon([[-5.8, 10], [-5, -1], [4, 2]], closed=True, color=violet11))
ax.add_patch(Polygon([[-5.8, 10], [-5, -1], [4, 2]], closed=True, color=violet13))
#8
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [4, -7.9]], closed=True, color=violet9))
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [4, -7.9]], closed=True, color=violet10))
ax.add_patch(Polygon([[6, 0], [-2, -7.9], [4, -7.9]], closed=True, color=violet10))
#9
ax.add_patch(Polygon([[6, 0], [8.2, -7.9], [4, -7.9]], closed=True, color=violet11))
ax.add_patch(Polygon([[6, 0], [8.2, -7.9], [4, -7.9]], closed=True, color=violet11))
#10
ax.add_patch(Polygon([[6, 0], [8.2, -7.9], [8.2, 3]], closed=True, color=violet12))
ax.add_patch(Polygon([[6, 0], [8.2, -7.9], [8.2, 3]], closed=True, color=violet12))
#11
ax.add_patch(Polygon([[6, 0], [3, 6.5], [8.2, 3]], closed=True, color=violet13))
ax.add_patch(Polygon([[6, 0], [3, 6.5], [8.2, 3]], closed=True, color=violet13))
#12
ax.add_patch(Polygon([[-2, 5], [3, 6.5], [2, 10]], closed=True, color=violet13))
ax.add_patch(Polygon([[-2, 5], [3, 6.5], [2, 10]], closed=True, color=violet13))
#13
ax.add_patch(Polygon([[-1.08, 6.15], [-5.8, 10], [2, 10]], closed=True, color=violet12))
ax.add_patch(Polygon([[-1.08, 6.15], [-5.8, 10], [2, 10]], closed=True, color=violet12))
#14
ax.add_patch(Polygon([[8.2, 10], [3, 6.5], [8.2, 3]], closed=True, color=violet14))
#15
ax.add_patch(Polygon([[8.2, 10], [3, 6.5], [2, 10]], closed=True, color=violet14))

# Кот
#1
ax.add_patch(Polygon([[-9.6, 9.6], [-4, 6.4], [-5.8, 4.6]], closed=True, color=color4))
#2
ax.add_patch(Polygon([[-9.6, 9.6], [-8.4, 2.5], [-5.8, 4.6]], closed=True, color=color1))
#3
ax.add_patch(Polygon([[-4, 6.4], [0,6.4], [-5.8, 4.6]], closed=True, color=color3))
#4
ax.add_patch(Polygon([[-3, 4], [0,6.4], [-5.8, 4.6]], closed=True, color=color2))
#5
ax.add_patch(Polygon([[-6.7, 2.3], [-8.4, 2.5], [-5.8, 4.6]], closed=True, color=color1))
#6
ax.add_patch(Polygon([[-3, 4], [-6.7, 2.3], [-5.8, 4.6]], closed=True, color=color3))
#7
ax.add_patch(Polygon([[-3, 4], [0,6.4], [-1.2, 3]], closed=True, color=color1))
#8
ax.add_patch(Polygon([[0.8, 4.5], [0,6.4], [-1.2, 3]], closed=True, color=color4))
#9
ax.add_patch(Polygon([[0.8, 4.5], [3.1,5.5], [0,6.4]], closed=True, color=color3))
#10
ax.add_patch(Polygon([[2.8,6.8], [3.1,5.5], [0,6.4]], closed=True, color=color5))
#12
ax.add_patch(Polygon([[7.8, 9.6], [2.8,6.8], [3.1,5.5]], closed=True, color=color3))
#13
ax.add_patch(Polygon([[7.8, 9.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color4))
#14
ax.add_patch(Polygon([[3.7, 1.6], [3.1,5.5], [6.4, 3.7]], closed=True, color=color1))
#15
ax.add_patch(Polygon([[-6.7, 2.3], [-8.4, 2.5], [-9, -0.8]], closed=True, color=color1))
#16
ax.add_patch(Polygon([[-9, -0.8], [-6.7, 2.3], [-6.4, 0.5]], closed=True, color=color1))
#17
ax.add_patch(Polygon([[-4.2, 0.9], [-6.7, 2.3], [-6.4, 0.5]], closed=True, color=color3))
#18
ax.add_patch(Polygon([[-6.7, 2.3], [-4.2, 0.9], [-3, 4]], closed=True, color=color4))
#19
ax.add_patch(Polygon([[-8.4, -3.6], [-6.4, 0.5], [-5, -1.6]], closed=True, color=color2))
#20
ax.add_patch(Polygon([[-9, -0.8], [-8.4, -3.6], [-6.4, 0.5]], closed=True, color=color1))
#21
ax.add_patch(Polygon([[-4.8, -4.7], [-8.4, -3.6], [-5, -1.6]], closed=True, color=color1))
#22
ax.add_patch(Polygon([[-4.8, -4.7], [-8.4, -3.6], [-7, -5.6]], closed=True, color=color1))
#23
ax.add_patch(Polygon([[-4.8, -4.7], [-4.3, -6.4], [-7, -5.6]], closed=True, color=color2))
#24
ax.add_patch(Polygon([[-4.8, -4.7], [-4.3, -6.4], [-1.2, -5.2]], closed=True, color=color3))
#25
ax.add_patch(Polygon([[-4.8, -4.7], [-2.6, -3.6], [-1.2, -5.2]], closed=True, color=color4))
#26
ax.add_patch(Polygon([[-4.8, -4.7], [-2.6, -3.6], [-3, -0.8]], closed=True, color=color1))
#27
ax.add_patch(Polygon([[-4.8, -4.7], [-5, -1.6], [-3, -0.8]], closed=True, color=color2))

#28 левый зрачок
ax.add_patch(Polygon([[-5, -0.1],[-4, -0.4] , [-4.2, 0.9]], closed=True, color=color2))
#29 левый зрачок
ax.add_patch(Polygon([[-5, -0.1],[-4, -0.4], [-5, -1.6]], closed=True, color=color1))

#30 левый глаз
ax.add_patch(Polygon([[-5, -0.1], [-6.4, 0.5], [-4.2, 0.9]], closed=True, color=violet2))
#31 левый глаз
ax.add_patch(Polygon([[-4, -0.4], [-5, -1.6], [-3, -0.8]], closed=True, color=violet3))
#32 левый глаз
ax.add_patch(Polygon([[-5, -0.1], [-6.4, 0.5], [-5, -1.6]], closed=True, color=violet1))
#33 левый глаз
ax.add_patch(Polygon([[-4, -0.4], [-3, -0.8], [-4.2, 0.9]], closed=True, color=violet6))

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
ax.add_patch(Polygon([[2.4, -4.7], [0.2, -3.6], [-1.2, -5.2]], closed=True, color=color5))
#42
ax.add_patch(Polygon([[2.4, -4.7], [2, -6.7], [-1.2, -5.2]], closed=True, color=color4))
#43
ax.add_patch(Polygon([[-1.1, -7.5], [2, -6.7], [-1.2, -5.2]], closed=True, color=color1))
#44
ax.add_patch(Polygon([[-1.1, -7.5], [-4.3, -6.4], [-1.2, -5.2]], closed=True, color=color1))
#45
ax.add_patch(Polygon([[2.4, -4.7], [0.2, -3.6], [0.5, -0.8]], closed=True, color=color2))
#46
ax.add_patch(Polygon([[-1.2, 3], [0.2, -3.6], [0.5, -0.8]], closed=True, color=color3))
#47
ax.add_patch(Polygon([[-1.2, 3], [1.9, 0.7], [0.5, -0.8]], closed=True, color=color2))
#48
ax.add_patch(Polygon([[0.8, 4.5],[1.9, 0.7] , [-1.2, 3]], closed=True, color=color5))
#49
ax.add_patch(Polygon([[0.8, 4.5],[1.9, 0.7] ,[3.1, 5.5] ], closed=True, color=color2))
#50
ax.add_patch(Polygon([[3.7, 1.6],[1.9, 0.7] ,[3.1, 5.5] ], closed=True, color=color3))
#51
ax.add_patch(Polygon([[3.7, 1.6],[1.9, 0.7] ,[4.1, 0.20 ]], closed=True, color=color4))
#52
ax.add_patch(Polygon([[2.4, -4.7], [2.7, -1.7], [0.5, -0.8]], closed=True, color=color3))

#53 правый зрачок
ax.add_patch(Polygon([[1.5, -0.45], [1.9, 0.7],[2.55,-0.2] ], closed=True, color=color2))
#54 правый зрачок
ax.add_patch(Polygon([[1.5, -0.45], [2.7, -1.7],[2.55,-0.2] ], closed=True, color=color1))

#55 правый глаз
ax.add_patch(Polygon([[1.5, -0.45], [1.9, 0.7], [0.5, -0.8]], closed=True, color=violet6))
#56 правый глаз
ax.add_patch(Polygon([[1.5, -0.45], [2.7, -1.7], [0.5, -0.8]], closed=True, color=violet3))
#58 правый глаз
ax.add_patch(Polygon([[2.55, -0.2],[1.9, 0.7]  , [4.1,0.2]], closed=True, color=violet2))
#57 правый глаз
ax.add_patch(Polygon([[2.55, -0.2], [2.7, -1.7], [4.1,0.2]], closed=True, color=violet1))

#57
ax.add_patch(Polygon([[3.7, 1.6], [6.9, 0.8], [6.4, 3.7]], closed=True, color=color2))
#58
ax.add_patch(Polygon([[3.7, 1.6], [6.9, 0.8], [4.1,0.2]], closed=True, color=color3))
#59
ax.add_patch(Polygon([[2.7, -1.7], [6.9, 0.8], [4.2, -3]], closed=True, color=color4))
#60
ax.add_patch(Polygon([[2.7, -1.7], [6.9, 0.8], [4.1,0.25]], closed=True, color=color3))
#61
ax.add_patch(Polygon([[2.7, -1.7],[2.4, -4.7] , [4.2, -3]], closed=True, color=color2))
#62
ax.add_patch(Polygon([[2, -6.7], [2.4, -4.7] , [4.2, -3]], closed=True, color=color3))
#63
ax.add_patch(Polygon([[6.8, -2.6],[6.9, 0.8] , [4.2, -3]], closed=True, color=color2))
#64
ax.add_patch(Polygon([[6.8, -2.6],[5, -5] , [4.2, -3]], closed=True, color=color1))
#65
ax.add_patch(Polygon([[2, -6.7],[5, -5] , [4.2, -3]], closed=True, color=color2))

plt.title('Рисунок кота')
plt.grid(False)
plt.show()