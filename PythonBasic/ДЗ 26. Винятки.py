import math


class NegativeStepError(Exception):
    pass


class Calculator:
    def __init__(self, one, operation, two):
        self.one = one
        self.operation = operation
        self.two = two

    def add(self):
        try:
            return self.one + self.two
        except Exception as exception:
            return f"Помилка: {exception}"

    def sub(self):
        try:
            return self.one - self.two
        except Exception as exception:
            return f"Помилка: {exception}"

    def mul(self):
        try:
            return self.one * self.two
        except Exception as exception:
            return f"Помилка: {exception}"

    def truediv(self):
        try:
            if self.two != 0:
                return self.one / self.two
            else:
                raise ZeroDivisionError("Ділення на нуль неможливе")
        except ZeroDivisionError as exception:
            return f"Помилка: {exception}"
        except Exception as exception:
            return f"Помилка: {exception}"

    def exponentiation(self):
        try:
            if self.two >= 0:
                return self.one ** self.two
            else:
                raise NegativeStepError("Від'ємний показник ступеня неможливий")
        except NegativeStepError as exception:
            return f"Помилка: {exception}"
        except Exception as exception:
            return f"Помилка: {exception}"

    def square_root(self):
        try:
            if self.one >= 0:
                return math.sqrt(self.one)
            else:
                raise ValueError("Корінь від від'ємного числа неможливий")
        except ValueError as exception:
            return f"Помилка: {exception}"
        except Exception as exception:
            return f"Помилка: {exception}"


try:
    one = float(input("Введіть перше значення: "))
    operation = input(
        "Введіть бажану операцію (+, -, *, /, **(зведення в ступінь), //(вилучення квадратного кореня)): ")
    two = float(input("Введіть друге значення: "))

    calculator = Calculator(one, operation, two)

    if calculator.operation == "+":
        print("Ваш результат: ", calculator.add())
    elif calculator.operation == "-":
        print("Ваш результат: ", calculator.sub())
    elif calculator.operation == "*":
        print("Ваш результат: ", calculator.mul())
    elif calculator.operation == "/":
        print("Ваш результат: ", calculator.truediv())
    elif calculator.operation == "**":
        print("Ваш результат: ", calculator.exponentiation())
    elif calculator.operation == "//":
        print("Ваш результат: ", calculator.square_root())
    else:
        print(f"Невірна операція ")

except ValueError:
    print("Помилка: Введені неправильні дані. Введіть числа для обчислення.")
