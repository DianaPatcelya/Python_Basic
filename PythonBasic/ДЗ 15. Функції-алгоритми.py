def main(analyze_number):
    if analyze_number.strip().lower() in ("вихід", "exit", "quit", "e", "q"):
        return "вихід"
    analyze_number = analyze_number.replace(',', '.')
    try:
        number = float(analyze_number)
        if number == 0:
            print("Ви ввели нуль")
        elif number > 0:
            if number.is_integer():
                print(f"Ви ввели позитивне ціле число: {int(number)}")
            else:
                print(f"Ви ввели позитивне дробове число: {number}")
        else:
            if number.is_integer():
                print(f"Ви ввели від'ємне ціле число: {int(number)}")
            elif number.is_integer() is False:
                print(f"Ви ввели від'ємне дробове число: {number}")
    except ValueError:
        print(f"Ви ввели неправильне число: {analyze_number}")


while True:
    user_request = input("Бажаєте ввести число на перевірку або вийти? "
                         "\nДля вихода введіть 'вихід', 'exit', 'quit', 'e' або 'q'\n")

    result = main(user_request)
    if result == "вихід":
        print("До зустрічі :)")
        break

