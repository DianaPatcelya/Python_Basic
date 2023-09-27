value_number = lambda number=(int(input("Введіть Ваше значення: "))): "нульове" if int(number) == 0 else ("парне" if int(number) % 2 == 0 else "непарне")
nnn_1 = value_number
print(f"Ви ввели {nnn_1()} число")
