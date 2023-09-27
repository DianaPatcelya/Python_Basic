repeat = True
while repeat:
    name = input("Введіть Ваше ім'я: ")
    age = input("Ваедіть Ваш вік: ")
    if not age.isdigit() or int(age) == 0:
        print("Помилка, повторіть введення.")
    elif 0 < int(age) < 10:
        print("Привіт, шкет", name)
    elif 10 <= int(age) < 18:
        print("Як справи, ", name, "?")
    elif 18 <= int(age) < 100:
        print("Що бажаєте, ", name, "?")
    elif int(age) > 100:
        print(name, ",ви брешете - у наш час стільки не живуть..")
    repeat = input("Бажаєте вийти? (Д/Y)").upper()
    if repeat == "Y":
        repeat = False
    if repeat == "Д":
        repeat = False
