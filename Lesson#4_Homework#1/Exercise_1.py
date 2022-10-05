"""1. Создать 3 переменные с одинаковыми данными (и одинаковым типом) и с одинаковыми идентификаторами (не присваивая
      значения переменных друг другу)
   2. Создать 2 переменные с одинаковыми данными (и одинаковым типом) и с разными идентификаторами
   3. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались одинаковые данные (и
      одинаковым типом), а у 2-х последних стали одинаковые идентификаторы и остались одинаковые данные.

    * добиться нужного результата необходимо только приведением типов данных к нужному"""

#  1.

x_1 = 5
x_2 = 5
x_3 = 5

print("#1\n", "x_1 ->", type(x_1), "\n", "x_2 ->", type(x_2), "\n", "x_3 ->", type(x_3))
print(" x_1 == x_2, x_1 == x_3, x_2 == x_3 ->", x_1 == x_2, x_1 == x_3, x_2 == x_3)
print(" x_1 is x_2, x_1 is x_3, x_2 is x_3 ->", x_1 is x_2, x_1 is x_3, x_2 is x_3, "\n")

#  2.

x_4 = [123]
x_5 = [123]

print("#2\n", "x_4 ->", type(x_4), "\n", "x_5 ->", type(x_5))
print(" x_4 == x_5 ->", x_4 == x_5)
print(" x_4 is x_5 ->", x_4 is x_5, "\n")

#  3

x_1 = float(x_1)
x_2 = float(x_2)
x_3 = float(x_3)

print("#3\n", "x_1 ->", type(x_1), "\n", "x_2 ->", type(x_2), "\n", "x_3 ->", type(x_3))
print(" x_1 == x_2, x_1 == x_3, x_2 == x_3 ->", x_1 == x_2, x_1 == x_3, x_2 == x_3)
print(" x_1 is x_2, x_1 is x_3, x_2 is x_3 ->", x_1 is x_2, x_1 is x_3, x_2 is x_3, "\n")

x_4 = int(*x_4)
x_5 = int(*x_5)

print(" x_4 =",x_4, "\n" " x_5 =", x_5)
print(" id(x_4) =", id(x_4), "\n" " id(x_5) =", id(x_5))
print(" x_4 ->", type(x_4), "\n" " x_5 ->", type(x_5))
print(" x_4 == x_5 ->", x_4 == x_5)
print(" x_4 is x_5 ->", x_4 is x_5)
