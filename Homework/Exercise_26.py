# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.


import math

class Calc():
    def __init__(self, num):
        try:
            self.num = float(num)
        except ValueError:
            print("Error. Экземпляр класса не должен иметь не числовое значение")
        except TypeError:
            print("Error. Экземпляр класса имеет значение недопустимого типа")

    def __add__(self, other):
        try:
            return self.num + float(other)
        except:
            print("Правое слагаемое невозможно перевести в цифровое значение")

    def __sub__(self, other):
        try:
            return self.num + float(other)
        except:
            print("Вычитаемое невозможно перевести в цифровое значение")

    def __mul__(self, other):
        try:
            return self.num * float(other)
        except:
            print("Множитель невозможно перевести в цифровое значение")

    def __truediv__(self, other):
        try:
            return self.num/float(other)
        except ZeroDivisionError:
            print("Деление на ноль не допускается")
            return 0
        except (ValueError, TypeError):
            print("Делитель невозможно перевести в число")

    def __pow__(self, other):
        try:
            return self.num ** int(other)
        except (ValueError, TypeError):
            print("У степени недопустимый тип")

    def sqr(self):
        try:
            return math.sqrt(self.num)
        except ValueError:
            print("Невозможно извлечь корень из отрицательного числа")
            return 0


d = Calc(10)
print("10 ** [] = ", d ** [])
print('10 ** "fgh" = ', d ** "fgh")
print("_" * 50)

Calc([])
Calc('for')
print("_" * 50)

print("d ** 'g' = ", d ** 'g')
print("d ** -4 = ", d ** -4)
print("_" * 50)

print("d/None = ", d/None)
print("d + '[]' = ", d + '[]')
print("_" * 50)

print("d * '[]' = ", d * '[]')
print("10 * '12' = ", d * '12')
print("_" * 50)

r = Calc(-4)
print(r.sqr())



