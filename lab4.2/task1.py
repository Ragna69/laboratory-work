import numpy as np

expenses = np.array([120, 135, 110, 100, 90, 80, 85, 95, 105, 115, 125, 135])

# Зимние месяцы
winter_months = [0, 1, 11]  #
winter_total = np.sum(expenses[winter_months])

# Летние месяцы
summer_months = [5, 6, 7]
summer_total = np.sum(expenses[summer_months])

if winter_total > summer_total:
    print("Зимой тратится больше на проезд.")
elif summer_total > winter_total:
    print("Летом тратится больше на проезд.")
else:
    print("Затраты на проезд одинаковы зимой и летом.")

# Поиск месяцев с максимальными расходами
max_value = np.max(expenses)
max_months = np.where(expenses == max_value)[0] + 1

print("Месяцы с наибольшими расходами:", max_months)
