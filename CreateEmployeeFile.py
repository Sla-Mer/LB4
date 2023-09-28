import csv
from faker import Faker
import random

# Ініціалізація генератора даних з вказаними налаштуваннями для України (UA)
fake = Faker('uk_UA')

# Кількість записів, які потрібно згенерувати
total_records = 2000

# Відсоток жіночої і чоловічої статі
female_percentage = 40
male_percentage = 60

# Заголовки для CSV-файлу
headers = ["Прізвище", "Ім'я", "По-батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]

# Списки по батькові для чоловіків і жінок
male_patronymics = ["Іванович", "Петрович", "Олександрович", "Володимирович", "Євгенович", "Михайлович", "Андрійович", "Сергійович", "Юрійович", "Аркадійович", "Вікторович", "Анатолійович", "Дмитрович", "Тимофійович", "Васильович", "Кузьмич", "Федорович", "Георгійович", "Ярославович", "Борисович"]
female_patronymics = ["Іванівна", "Петрівна", "Олександрівна", "Володимирівна", "Євгенівна", "Михайлівна", "Андріївна", "Сергіївна", "Юріївна", "Аркадіївна", "Вікторівна", "Анатоліївна", "Дмитрівна", "Тимофіївна", "Василівна", "Кузьмівна", "Федорівна", "Георгіївна", "Ярославівна", "Борисівна"]

# Генерування записів і запис до CSV-файлу
with open('employees.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(headers)
    for _ in range(total_records):
        gender = random.choices(['Чоловік', 'Жінка'], weights=[male_percentage, female_percentage])[0]

        if gender == 'Чоловік':
            last_name = fake.last_name_male()
            first_name = fake.first_name_male()
            patronymic = random.choice(male_patronymics)
        else:
            last_name = fake.last_name_female()
            first_name = fake.first_name_female()
            patronymic = random.choice(female_patronymics)

        birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85)
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()

        row = [last_name, first_name, patronymic, gender, birthdate, position, city, address, phone_number, email]
        csv_writer.writerow(row)

print(f"Згенеровано {total_records} записів та збережено у файл employees.csv.")
