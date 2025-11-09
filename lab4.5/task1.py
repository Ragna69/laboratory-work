import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Настройки
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (14, 6)

# Загрузка данных
df = pd.read_excel("lab_4_part_5.xlsx", header=1)
df.columns = df.columns.str.strip()
df['Дата'] = pd.to_datetime(df['Дата'], dayfirst=True)

# Базовые расчёты
df['Цена'] = df['Продажи'] / df['Количество']
df['Маржа'] = df['Продажи'] - df['Себестоимость']
df['Месяц'] = df['Дата'].dt.to_period('M')

# Группировка
помесячно = df.groupby(['Месяц', 'товар']).agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum'
}).reset_index()

помесячно['Средняя_цена'] = помесячно['Продажи'] / помесячно['Количество']
помесячно['Маржа'] = помесячно['Продажи'] - помесячно['Себестоимость']

# === Общий товарооборот ===
товарооборот = df.groupby('Месяц')['Продажи'].sum().reset_index()
plt.figure()
plt.plot(товарооборот['Месяц'].astype(str), товарооборот['Продажи'], marker='o')
plt.title("Общий товарооборот по месяцам")
plt.ylabel("Сумма продаж")
plt.xticks(rotation=45)
plt.locator_params(axis='y', nbins=10)
plt.ylim(товарооборот['Продажи'].min() * 0.95, товарооборот['Продажи'].max() * 1.05)
plt.tight_layout()
plt.show()

# === Продажи по товарам ===
товары = df['товар'].unique()
plt.figure(figsize=(14, 6))
все_продажи = []
for товар in товары:
    подтаблица = помесячно[помесячно['товар'] == товар]
    все_продажи.extend(подтаблица['Продажи'].dropna().values)
    plt.plot(подтаблица['Месяц'].astype(str), подтаблица['Продажи'], marker='o', label=товар)

plt.title("Продажи по каждому виду товара")
plt.xlabel("Месяц")
plt.ylabel("Сумма продаж")
plt.xticks(rotation=45)
plt.locator_params(axis='y', nbins=10)
plt.ylim(min(все_продажи) * 0.95, max(все_продажи) * 1.05)
plt.legend()
plt.tight_layout()
plt.show()

# === Средняя цена ===
plt.figure(figsize=(14, 6))
все_цены = []
for товар in товары:
    подтаблица = помесячно[помесячно['товар'] == товар]
    все_цены.extend(подтаблица['Средняя_цена'].dropna().values)
    plt.plot(подтаблица['Месяц'].astype(str), подтаблица['Средняя_цена'], marker='o', label=товар)

plt.title("Средняя цена по каждому товару")
plt.xlabel("Месяц")
plt.ylabel("Цена")
plt.xticks(rotation=45)
plt.locator_params(axis='y', nbins=10)
plt.ylim(min(все_цены) * 0.95, max(все_цены) * 1.05)
plt.legend()
plt.tight_layout()
plt.show()

# === Маржа ===
plt.figure(figsize=(14, 6))
все_маржи = []
for товар in товары:
    подтаблица = помесячно[помесячно['товар'] == товар]
    все_маржи.extend(подтаблица['Маржа'].dropna().values)
    plt.plot(подтаблица['Месяц'].astype(str), подтаблица['Маржа'], marker='s', linestyle='--', label=товар)

plt.title("Маржа по каждому товару")
plt.xlabel("Месяц")
plt.ylabel("Маржа")
plt.xticks(rotation=45)
plt.locator_params(axis='y', nbins=10)
plt.ylim(min(все_маржи) * 0.95, max(все_маржи) * 1.05)
plt.legend()
plt.tight_layout()
plt.show()

# === Продажи по точкам реализации ===
по_точкам = df.groupby(['Месяц', 'точка']).agg({
    'Количество': 'sum',
    'Продажи': 'sum'
}).reset_index()

сводная = по_точкам.pivot(index='Месяц', columns='точка', values='Продажи')
сводная.index = сводная.index.astype(str)
ax = сводная.plot(marker='o', figsize=(14, 6))
ax.set_title("Продажи по точкам реализации")
ax.set_ylabel("Сумма продаж")
plt.xticks(rotation=45)
plt.locator_params(axis='y', nbins=10)
plt.ylim(сводная.min().min() * 0.95, сводная.max().max() * 1.05)
plt.tight_layout()
plt.show()

# === Прогноз продаж ===
plt.figure(figsize=(14, 6))
все_факт = []
все_прогноз = []
for товар in товары:
    подтаблица = помесячно[помесячно['товар'] == товар].copy()
    подтаблица['Период'] = range(len(подтаблица))
    x = подтаблица['Период'].values
    y = подтаблица['Продажи'].values
    коэф = np.polyfit(x, y, deg=1)
    тренд = np.poly1d(коэф)
    будущее_x = np.arange(len(x), len(x) + 3)
    будущее_y = тренд(будущее_x)

    все_факт.extend(y)
    все_прогноз.extend(будущее_y)

    plt.plot(x, y, 'o-', label=f"{товар} — факт")
    plt.plot(будущее_x, будущее_y, 's--', label=f"{товар} — прогноз")

plt.title("Прогноз продаж по каждому товару")
plt.xlabel("Период")
plt.ylabel("Сумма продаж")
plt.locator_params(axis='y', nbins=10)
plt.ylim(min(все_факт + list(все_прогноз)) * 0.95, max(все_факт + list(все_прогноз)) * 1.05)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
