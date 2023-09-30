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
        return

    def stop(self):
        print("stop")


car = Auto(brand="Hyundai", age=10, mark="Santa Fe", color="black", weight=1585)

print(f"Brand: {car.brand}, Age: {car.age}, Color: {car.color}, Mark: {car.mark}, Weight: {car.weight}")
car.move()
car.stop()
car.birthday()
print(f"New Age: {car.age}")

car_2 = Auto(age=7, brand="BMW", mark="iX1", weight=2085)
print(f"Brand: {car_2.brand}, Age: {car_2.age}, Weight: {car_2.weight}")
