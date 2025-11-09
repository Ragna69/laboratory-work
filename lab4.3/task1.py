import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Настройки
np.random.seed(42)
random.seed(42)

# Справочники
years = [2021, 2022, 2023, 2024, 2025]
forms = ['очная', 'заочная']
specialties = ['Информатика', 'Физика', 'Математика', 'Экономика', 'Биология']
cities = ['Минск', 'Гомель', 'Брест', 'Гродно', 'Могилёв', 'Витебск']
streets = ['Ленина', 'Советская', 'Победы', 'Мира', 'Парковая', 'Школьная']

# Генерация ФИО
def generate_fio():
    first_names = ['Алексей', 'Мария', 'Иван', 'Ольга', 'Дмитрий', 'Анна']
    last_names = ['Иванов', 'Петрова', 'Сидоров', 'Кузнецова', 'Смирнов', 'Васильева']
    patronymics = ['Алексеевич', 'Ивановна', 'Сергеевич', 'Павловна', 'Владимирович', 'Николаевна']
    return f"{random.choice(last_names)} {random.choice(first_names)} {random.choice(patronymics)}"

# Генерация адреса
def generate_address():
    return f"{random.choice(cities)}, ул. {random.choice(streets)}, д. {random.randint(1, 100)}"

# Генерация телефона
def generate_phone():
    return f"+375 (29) {random.randint(1000000, 9999999)}"

# Генерация данных
data = []
for _ in range(1000):
    fio = generate_fio()
    year = random.choice(years)
    form = random.choice(forms)
    math = np.random.randint(30, 100)
    physics = np.random.randint(30, 100)
    russian = np.random.randint(30, 100)
    attest = np.round(np.random.uniform(5.0, 10.0), 2)
    total = math + physics + russian + attest * 10
    spec = random.choice(specialties)
    address = generate_address()
    phone = generate_phone()
    data.append([fio, year, form, math, physics, russian, attest, total, spec, address, phone])

# Создание DataFrame
columns = ['ФИО', 'Год', 'Форма', 'Математика', 'Физика', 'Русский', 'Аттестат', 'Общий балл', 'Специальность', 'Адрес', 'Телефон']
df = pd.DataFrame(data, columns=columns)


# Средние баллы по предметам по годам
for subject in ['Математика', 'Физика', 'Русский']:
    df.groupby('Год')[subject].mean().plot(marker='o', label=subject)
plt.title(' Средний балл ЦТ по предметам')
plt.xlabel('Год')
plt.ylabel('Балл')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Средний балл аттестата по годам
df.groupby('Год')['Аттестат'].mean().plot(marker='s', color='purple')
plt.title(' Средний балл аттестата по годам')
plt.xlabel('Год')
plt.ylabel('Балл')
plt.grid(True)
plt.tight_layout()
plt.show()

# Минимальный проходной балл по годам
df.groupby('Год')['Общий балл'].min().plot(marker='^', color='red')
plt.title(' Минимальный проходной балл по годам')
plt.xlabel('Год')
plt.ylabel('Общий балл')
plt.grid(True)
plt.tight_layout()
plt.show()

# Количество студентов по специальностям
df['Специальность'].value_counts().plot(kind='bar', color='teal')
plt.title(' Количество студентов по специальностям')
plt.xlabel('Специальность')
plt.ylabel('Количество')
plt.tight_layout()
plt.show()

# Распределение по формам обучения
df['Форма'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Распределение по формам обучения')
plt.ylabel('')
plt.tight_layout()
plt.show()

