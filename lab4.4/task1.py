import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Настройки
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (15, 12)

# Загрузка и подготовка данных
df = pd.read_excel("s7_sales.xlsx", sheet_name="DATA")
df.columns = ['ISSUE_DATE', 'FLIGHT_DATE_LOC', 'PAX_TYPE', 'REVENUE_AMOUNT', 'FOP_TYPE_CODE',
              'ORIG_CITY_CODE', 'DEST_CITY_CODE', 'ROUTE_FLIGHT_TYPE', 'FFP_FLAG', 'SALE_TYPE']
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
df['month'] = df['FLIGHT_DATE_LOC'].dt.month
df['year'] = df['FLIGHT_DATE_LOC'].dt.year

#───Общая статистика───
print("───ОБЩАЯ СТАТИСТИКА───")
print(df.describe(include='all'))

#───Сезонная агрегация───
monthly_stats = df.groupby(['year', 'month']).agg({
    'REVENUE_AMOUNT': 'sum',
    'FLIGHT_DATE_LOC': 'count'
}).rename(columns={'FLIGHT_DATE_LOC': 'FLIGHT_COUNT'}).reset_index()

#───Прогноз через numpy───
monthly_stats['period'] = range(len(monthly_stats))
x = monthly_stats['period'].values
y = monthly_stats['REVENUE_AMOUNT'].values
coeffs = np.polyfit(x, y, deg=1)
trend = np.poly1d(coeffs)
future_x = np.arange(len(x), len(x) + 3)
future_y = trend(future_x)
rmse = np.sqrt(np.mean((trend(x) - y) ** 2))

#───Общая фигура с 5 графиками───
fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# 1. Топ-10 аэропортов
top_airports = df['ORIG_CITY_CODE'].value_counts().head(10)
axes[0, 0].bar(top_airports.index, top_airports.values, color='skyblue')
axes[0, 0].set_title("Топ-10 аэропортов по вылетам")
axes[0, 0].set_xlabel("Аэропорт")
axes[0, 0].set_ylabel("Количество")
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Сезонность по продажам
for year in sorted(df['year'].unique()):
    subset = monthly_stats[monthly_stats['year'] == year]
    axes[0, 1].plot(subset['month'], subset['REVENUE_AMOUNT'], marker='o', label=str(year))
axes[0, 1].set_title("Сезонность по продажам")
axes[0, 1].set_xlabel("Месяц")
axes[0, 1].set_ylabel("Сумма")
axes[0, 1].legend()

# 3. Сезонность по перелётам
for year in sorted(df['year'].unique()):
    subset = monthly_stats[monthly_stats['year'] == year]
    axes[1, 0].plot(subset['month'], subset['FLIGHT_COUNT'], marker='o', label=str(year))
axes[1, 0].set_title("Сезонность по перелётам")
axes[1, 0].set_xlabel("Месяц")
axes[1, 0].set_ylabel("Количество")
axes[1, 0].legend()

# 4. Типы пассажиров
sns.boxplot(x='PAX_TYPE', y='REVENUE_AMOUNT', data=df, ax=axes[1, 1])
axes[1, 1].set_title("Сумма покупки по типу пассажира")

# 5. Прогноз продаж
axes[2, 0].plot(x, y, 'o-', label='Факт')
axes[2, 0].plot(future_x, future_y, 's--', label='Прогноз')
axes[2, 0].set_title("Прогноз продаж")
axes[2, 0].set_xlabel("Период")
axes[2, 0].set_ylabel("Сумма")
axes[2, 0].legend()

# 6. Пустая ячейка
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()

#───Отдельное полотно: способы оплаты───
plt.figure(figsize=(10, 6))
fop_order = df['FOP_TYPE_CODE'].value_counts().index
sns.countplot(y='FOP_TYPE_CODE', data=df, order=fop_order, palette='viridis')
plt.title("Способы оплаты")
plt.xlabel("Количество")
plt.ylabel("Тип оплаты")
plt.tight_layout()
plt.show()

#───Финальный вывод───
print("\n───ПРОГНОЗ───")
print(f"RMSE прогноза: {rmse:.2f}")
print(f"Прогноз на следующие периоды: {future_y.round(2)}")
