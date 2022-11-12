# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math
from Exercise_23_dop import Point


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
         return "Circle" + super().__str__()[5:] + f", radius = {self.radius}"

    def area(self):
        return math.pi * self.radius**2

    def sircle_weight(self):
        return 2*math.pi*self.radius

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y) if radius != 0 else Point(x, y)
        # else (super().__str__()[0:4] + f"({x}, {y})") - выводит класс str
        # else super().__str__ - выводит значения не x, y, а self,x и self.y


a = Circle(10, 2, 3)
b = Circle(4, 5, 7)
z = a + b

print(a)
print(b)
print(z)

f = Circle(6, 7, 9)
g = Circle(7, 2, 12)
h = f - g
print(h, type(h))

v = Circle(5, 7, 10)
n = Circle(5, 4, 6)
m = v - n
print(m, type(m))





