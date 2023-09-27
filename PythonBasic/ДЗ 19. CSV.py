import json
import csv
import random

with open('ДЗ_18.json') as f:
    out_json = json.load(f)


def operator():
    list_code = ['095', '066', '098', '096', '050', '097']
    code = random.choice(list_code)
    return code


def numb():
    number_tel = (random.randint(0000000, 9999999))
    return number_tel


def phone_number():
    ph_num = f"{operator()}{numb()}"
    return ph_num


for key, value in out_json.items():
    has_phone = random.choices([True, False], [0.75, 0.25])[0]
    if has_phone:
        value.append(phone_number())

with open('ДЗ_19.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')

    csv_writer.writerow(['ІД', 'Ім\'я', 'Вік', 'Телефон'])
    for key, value in out_json.items():
        csv_writer.writerow([key] + value)

print("Дані користувача: ІД, Ім'я, Вік, Телефон")
