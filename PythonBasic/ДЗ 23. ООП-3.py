import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return 'Circle' + super().__str__()[5:-1] + f', radius={self.radius})'

    def __sub__(self, other):
        radius_diff = abs(self.radius - other.radius)

        if radius_diff == 0:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Circle(radius_diff, self.x, self.y)


circle_1 = Circle(0, 1, 2)
circle_2 = Circle(0, 3, 4)
result = circle_1 - circle_2

# print(type(result))
if type(result) == Point:
    print(f"Різниця віднімання двох кіл - точки: {result.x}, {result.y}")
else:
    print(f"Різниця віднімання двох кіл - коло з радіусом {result.radius}")
