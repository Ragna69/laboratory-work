# сгенерировать самим продукцию буфета: булочка, пирожки, смаженки, количество которое привезли,
# количество которое продали и цену, посчитать остаток еды, посчитать выручку по каждой позиции за день,
# используя библиотеки, посчитать сколько оcталось и сколько продали
# дальше визуализация, сколько было продано по каждому продукту, выручка за день

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Продукт": ["Булочка", "Пирожок", "Смаженка", "Пицца"],
    "Привезли": [120, 150, 100, 110],
    "Продали": [90, 130, 80, 70],
    "Цена": [1.5, 2.0, 2.5, 3.0]
}

df = pd.DataFrame(data)

df["Остаток"] = df["Привезли"] - df["Продали"]
df["Выручка"] = df["Продали"] * df["Цена"]

total_sold = df["Продали"].sum()
total_left = df["Остаток"].sum()
total_revenue = df["Выручка"].sum()

print("Итоговая таблица:")
print(df)
print("\nВсего продано:", total_sold)
print("Всего осталось:", total_left)
print("Общая выручка:", total_revenue)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.barplot(x="Продукт", y="Продали", data=df, palette="viridis")
plt.title("Продано по каждому продукту")
plt.ylabel("Количество")

plt.subplot(1,2,2)
sns.barplot(x="Продукт", y="Выручка", data=df, palette="magma")
plt.title("Выручка по каждому продукту")
plt.ylabel("Рубли")

plt.tight_layout()
plt.show()

