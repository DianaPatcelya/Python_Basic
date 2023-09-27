import random


def main():
    def assay_win():
        if number == numder_comp:
            return assay_win

    def assay_less():
        if number > numder_comp:
            return assay_less

    def assay_more():
        if number < numder_comp:
            return assay_more

    while True:
        print("Вгадай числo від 1 до 10")
        numder_comp = random.randint(1, 10)
        user_attempts = 3

        while user_attempts > 0:
            number = int(input("Введіть Ваше число: "))
            user_attempts -= 1
            if assay_less():
                print("Потрібне менше число")
            elif assay_more():
                print("Потрібне більше число")
            elif assay_win():
                print("Ти виграв!")
                break

        print('Пограємо ще? (Натисни Y)')
        repeat = input().upper()
        if repeat != "Y":
            break


main()
