import time


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print("attention")
        super().move()
        print(f"max speed is {self.max_speed}")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


bmw = Car("BmW", 2, "OOO", 260, color="Red")
opel = Car("Opel", 5, "Vivaro", 210, None, 250)
bmw.load()
bmw.move()
print(opel.weight)

print("*" * 50)

mercedes = Truck("Mercedes", 7, "truck", 1500, color="Green")
audi = Truck("Audi", 12, "Xi5", 450, "Red", None)
mercedes.load()
mercedes.move()
print(f"Mark audi: {audi.mark} and Max load mercedes: {mercedes.max_load}")
