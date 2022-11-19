# Создайте свой произвольный класс и в нём помимо обычных методов
# и атрибутов создайте несколько статических методов и методов класса.
#
# Продемонстрируйте их работу.

import math

class Geometry():
    TOTAL_OBJECT = 0
    TOTAL_SUM = 0
    TOTAL_MAX = 10

    def __init__(self, x: (int, float), y: (int, float)):
        self.x = x
        self.y = y
        Geometry.TOTAL_OBJECT += 1

    def quadrant(self):
        if self.x == 0 or self.y == 0:
            return "Точка расположена в центре координат или на одной из осей"
        elif self.x < 0:
            if self.y > 0:
                return "Точка расположена в квадранте II"
            else:
                return "Точка расположена в квадранте III"
        elif self.y > 0:
            return "Точка расположена в квадранте I"
        else:
            return "Точка расположена в квадранте IV"

    def square_area(self):
        if self.x <= 0 or self.y <= 0:
            return "Значения заданы не верно, одно из них отрицательное или равно нулю"
        else:
            return self.x * self.y

    def __sub__(self, other):
        Geometry.TOTAL_SUM += 1
        if self.x <= 0 or self.y <= 0 or other.x <= 0 or other.y<= 0:
            return "Расчет не корректен, один из аргументов отрицательный или равен нулю"
        else:
            z = self.x * self.y - other.x * other.y
            return z if z >= 0 else f"Площадь квадрата №1 меньше квадрата №2 на {abs(z)}"

    @classmethod
    def total_objects(cls):
        print(f"Создано экземпляров класса: {cls.TOTAL_OBJECT}")
        print(f"Количество обращений для расчета разности площадей квадратов: {cls.TOTAL_SUM}")

    @classmethod
    def check_ex(cls):
        if Geometry.TOTAL_MAX > Geometry.TOTAL_OBJECT:
            return f"Количество экземпляров класса меньше установленного значения {Geometry.TOTAL_MAX} единиц"
        else:
            return f"Количество экземпляров класса достигло установленного значения {Geometry.TOTAL_MAX} единиц"

    @staticmethod
    def sqr_PI():
        return math.sqrt(math.pi)

    # длина вектора в квдрате
    @staticmethod
    def normal(x: (int, float), y: (int, float)):
        return x*x + y*y


figura_1 = Geometry(-1, 5)
figura_2 = Geometry(7, 8)
figura_3 = Geometry(2, 1)
figura_4 = Geometry(-3, -6)

print("-" * 50)
print("Разность площадей квадратов:", figura_1-figura_2)
print("Разность площадей квадратов:", figura_2-figura_3)
print("-" * 50)

print(figura_4.quadrant())
print(figura_3.quadrant())
print("-" * 50)

print("Площадь квадрата: ", figura_3.square_area())
print("-" * 50)

print("Корень квадратынй из числа pi: ", "%.2f" % figura_4.sqr_PI())
print("Корень квадратынй из числа pi: ", "%.2f" % Geometry.sqr_PI())
print("-" * 50)

print("Вектор в квадрате: ", Geometry.normal(3, 6))
print("Вектор в квадрате: ", figura_3.normal(7, 9))
print("-" * 50)

print(Geometry.check_ex())
print("-" * 50)

Geometry.total_objects()
print("-" * 50)

print(Geometry.mro())
