numb = (input("Введіть Ваше значення: "))
if not numb.isdigit():
    print("Помилка, повторіть введення: ")
else:
    numb_form = "нульове" if int(numb) == 0 else ("парне" if int(numb) % 2 == 0 else "непарне")
    print(f"Ви ввели {numb_form} число")
