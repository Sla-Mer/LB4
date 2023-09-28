import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані з CSV-файлу
try:
    df = pd.read_csv('employees.csv', sep=';', encoding='utf-8-sig')
except FileNotFoundError:
    print("Повідомлення про відсутність або проблеми при відкритті файлу CSV")
    exit()

# Виводимо повідомлення про успішне відкриття файлу
print("Ok")

# Функція для розрахунку віку за датою народження
def calculate_age(birthdate):
    today = pd.to_datetime('today')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Рахуємо кількість співробітників чоловічої і жіночої статі
gender_counts = df['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_counts)

# Побудова діаграми для статі
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title("Розподіл співробітників за статтю")
plt.show()

# Рахуємо кількість співробітників в кожній віковій категорії
def categorize_age(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age < 45:
        return "18-45"
    elif 45 <= age < 70:
        return "45-70"
    else:
        return "older_70"

df['Вік'] = df['Дата народження'].apply(lambda x: calculate_age(pd.to_datetime(x)))
age_category_counts = df['Вік'].apply(lambda x: categorize_age(x)).value_counts()
print("\nКількість співробітників за віковою категорією:")
print(age_category_counts)

# Побудова діаграми для вікових категорій
plt.figure(figsize=(8, 6))
age_category_counts.plot(kind='bar')
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.title("Розподіл співробітників за віковою категорією")
plt.show()

# Рахуємо кількість співробітників чоловічої і жіночої статі в кожній віковій категорії
gender_age_counts = df.groupby(['Стать', df['Вік'].apply(categorize_age)]).size().unstack(fill_value=0)
print("\nКількість співробітників за статтю та віковою категорією:")
print(gender_age_counts)

# Побудова діаграм для статі та вікових категорій
gender_age_counts.plot(kind='bar', stacked=True)
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.title("Розподіл співробітників за статтю та віковою категорією")
plt.show()
