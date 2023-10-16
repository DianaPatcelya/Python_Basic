from person import Person
from person_database import Database
from datetime import datetime

db = Database()

while True:
    print("Меню:")
    print("1. Завантажити дані з файлу")
    print("2. Додати нову людину")
    print("3. Зберегти дані у файл")
    print("4. Пошук за ім\"ям, прізвищем або по батькові")
    print("5. База даних")
    print("6. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        filename = input("Введіть ім'я файлу для завантаження: ")
        db.load_from_excel(filename)
        print(f"Дані завантажено з файлу.")

    elif choice == "2":
        first_name = input("Введіть ім'я: ")
        last_name = input("Введіть прізвище: ")
        middle_name = input("Введіть по батькові: ")
        birth_date = input("Введіть дату народження (у форматі 01.01.2023): ")
        death_date = input("Введіть дату смерті (якщо є, у форматі 01.01.2023, інакше натисніть Enter): ")
        gender = input("Введіть стать (m або f): ")

        if death_date:
            death_date_obj = datetime.strptime(death_date, "%d.%m.%Y")
            birth_date_obj = datetime.strptime(birth_date, "%d.%m.%Y")
            if death_date_obj < birth_date_obj:
                print("Помилка: Дата смерті не може бути раніше за дату народження.")
                continue

        person = Person(first_name, gender, birth_date, last_name, middle_name, death_date)
        db.add_person(person)
        print("Дані користувача були записані.")

    elif choice == "3":
        filename = input("Введіть ім'я файлу для збереження: ")
        db.save_to_excel(filename)
        print(f"Дані збережено у файл.")

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
