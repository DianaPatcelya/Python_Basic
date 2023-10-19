from person import Person
from person_database import Database
from datetime import datetime

db = Database()

while True:
    print("Меню:")
    print("1. Завантажити дані з файлу")
    print("2. Додати нову людину")
    print("3. Зберегти дані у файл")
    print("4. Пошук за ім'ям, прізвищем або по батькові")
    print("5. База даних")
    print("6. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        try:
            filename = input("Введіть ім'я файлу для завантаження: ")
            db.load_from_excel(filename)
            print(f"Дані завантажено з файлу '{filename}'.")
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено.")

    elif choice == "2":
        try:
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            middle_name = input("Введіть по батькові: ")

            current_date = datetime.now()

            birth_date_input = input("Введіть дату народження (у форматі 01.01.2023): ")
            birth_date = Person.change_date(birth_date_input, current_date)

            death_date = None

            death_input = input("Введіть дату смерті (якщо є, у форматі 01.01.2023, інакше натисніть Enter): ")
            if death_input:
                death_date = Person.change_date(death_input, current_date)

            gender = input("Введіть стать (m або f): ")

            person = Person(first_name, gender, birth_date, last_name, middle_name, death_date)
            db.add_person(person)

            print("Дані користувача були записані.")

        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, введіть коректні дані.")

    elif choice == "3":
        try:
            filename = input("Введіть ім'я файлу для збереження: ")
            db.save_to_excel(filename)
            print(f"Дані збережено у файл '{filename}'.")
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не може бути створений або перезаписаний.")

    elif choice == "4":
        query = input("Введіть рядок для пошуку: ")
        results = db.search_people(query)
        if results:
            for result in results:
                print(result)
        else:
            print("Нічого не знайдено за вашим запитом.")

    elif choice == "5":
        print("База даних:")
        for person in db.people:
            print(person)

    elif choice == "6":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Будь ласка, виберіть опцію з меню.")
