"""# 1

print("Silence is golden")
"""
"""# 2

print("Четверг")
print("Октябрь")
print("Всеволод")
"""

"""# 3

for i in range(5):
    print("0"*(i+1))"""

"""# 4

for i in range(5):
    print("A"*8)"""

"""# 5

print("W     W     W")
print(" W   W W   W")
print("  W W   W W")
print("   W     W")"""

"""# 6

print("1+2-4=",1 + 2 -4)"""

"""# 7
print("1/2+1/4=", 1/2+1/4)"""

"""# 8

a = 2
b = 3
x = (a + 4 * b) * (a - 3 * b) + a ** 2
print("x=", x)"""

"""# 9

x = -2
y = abs(x) + x ** 5
print("y=", y)"""

"""# 10

for x in (1.7, 3):
    y = (x + 1) ** 2 + 3 * (x + 1)
    print("y=", y)"""

"""# 11

import math

x = -2.34
y = (abs(x - 5) - math.sin(x))/3 + ((x ** 2 + 2014) ** 0.5 * math.cos(2 * x)) - 3
print("y=", y)"""

"""# 12

import math

x = 3.6
y = math.exp(x - 2) + abs(math.sin(x)) - x ** 4 * math.cos(1 / x)
print("y=", y)"""

"""# 13

import math

x = 1
a = 0.1
b = 0.2

y = (x ** 2 + b) ** (1 / 5) - b **2 * (math.sin(x + a)) ** 3 / x
print("y=", y)"""

"""# 14

x = float(input("Введите x="))
y = float(input("Введите y="))
w = x + y
z = x * y

print("x+y=", w)
print("x*y=", z)"""

"""# 15

x = float(input("Введите число x="))

w = x ** 2
z = x ** 3

print("x в квадрате равен", w)
print("x в кубе равен", z)"""

"""# 16

x = float(input("Введите x="))
y = float(input("Введите y="))
z = float(input("Введите z="))
w = x * 2
e = y - 3
r = z ** 2

massiv_add = w + e + r
print("сумма обработанных числе =", massiv_add)
"""

"""# 17
# Пользователь вводит три числа. Найдите среднее арифметическое этих чисел, а также разность удвоенной суммы первого
# и третьего чисел и утроенного второго числа.

x = float(input("Введите x="))
y = float(input("Введите y="))
z = float(input("Введите z="))

massiv_add = (x + y + z)/3
s = (x + z) * 2 - y * 3

print("Среднее арифметическое =", massiv_add)
print("Расчетное значение = ", s)"""

"""# 18

x = float(input("Введите значение стороны квадрата = "))
s = x ** 2
p = x * 4

print("Площадь квадрата = ", s)
print("Периметр квадрата = ", p)"""

"""# 19
# Пользователь вводит цены 1 кг конфет и 1 кг печенья. Найдите стоимость: а) одной покупки из 300 г конфет и
# 400 г печенья; б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.

x = float(input("Введите стоиомсть 1 кг конфет, грн = "))
y = float(input("Введите стоиомсть 1 кг печенья, грн = "))

z = x * 0.3 + y * 0.4
c = 3 * (x * 1.8 + y * 2)

print("Cтоимость одной покупки из 300 г конфет и 400 г печенья = " + str(z), ",грн")
print("Cтоимость трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет = " + str(c), ",грн")"""

"""# 20

x = float(input("Введите время, мин = "))
y = float(input("Введите расстояние, км = "))

z = y * 1000/x

print("Скорость = ", z, "м/мин")"""

"""# 21
# Даны катеты прямоугольного треугольника. Найдите площадь, периметр и гипотенузу треугольника.

import math
x = float(input("Введите катет а треугольника, см = "))
y = float(input("Введите катет b треугольника, см км = "))

c = math.sqrt(x ** 2 + y ** 2)
p = (x + y) * 2
s = x * y / 2

print("Гипотенуза треугольника с = ", c, ",см")
print("Периметр треугольника P = ", p, ",см")
print("Площадь треугольника S = ", s, ",см2")"""

"""# 22
# Дано значение температуры в градусах Цельсия. Вывести температуру  в градусах Фаренгейта.

x = float(input("Введите значение температуры в °C = "))

t_F = x * 1.8 + 32

print("Температура в Фаренгейтах =", t_F, "°F")
"""
"""# 23
# Известно, что x кг конфет стоит a рублей. Определите, сколько стоит y кг этих конфет, а также сколько кг
# конфет можно купить на k рублей. Все значения вводит пользователь.

x = float(input("Введите количество ранее купленных конфет, кг x = "))
a = float(input("Введите стоимость ранее купленных конфет, грн a = "))
y = float(input("Введите количество конфет, которые предполагается купить, кг y = "))
k = float(input("Введите количество имеющихся денег, грн k = "))

s = a / x
b = s * y
v = k / s

print("Стоимость 1 кг конфет составляет", s, "грн")
print("Стоимость", y, " кг конфет составляет", b, "грн")
print("На", k, "грн", "возможно купить", v, "кг конфет")"""

"""# 24
# Пользователь вводит количество дней, указывает процент скидки и вводит сумму. Рассчитать прибыль, если за каждый день
# сумма увеличивается на 3 $  и затем применяется скидка, то есть итоговая сумма еще увеличивается на данное число
# процентов.

x = float(input("Введите количество дней = "))
a = float(input("Введите процент, % = "))
y = float(input("Введите сумму, $ = "))

pr = (x * 3 + y) * (100 + a)/100 - y

print("Прибыл за", x, "дней составляет", pr, "$")"""

"""# 25
# Пользователь вводит количество недель, месяцев, лет и получает количество дней за это время.
# Считать, что в месяце 30 дней.

x = int(input("Введите количество недель = "))
a = int(input("Введите количество месяцев = "))
y = int(input("Введите количество лет = "))

l = x * 7 + a * 30 + y * 365

print("Количество дней составляет =", l)"""

"""# 26

x = float(input("Введите число x = "))
y = float(input("Введите число y = "))

x, y = y, x

print("x =", x, "y =", y)"""

"""# 27
# Даны три переменные a, b и c. Изменить значения этих переменных так, чтобы в a хранилось значение a+b,
# в b хранилась разность старых значений c−a, а в c хранилось сумма старых значений a+b+c. Например,
# a=0, b=2, c=5, тогда новые значения a=2, b=5 и c=7.

a = float(input("Введите число a = "))
b = float(input("Введите число b = "))
c = float(input("Введите число c = "))

massiv_add = [a, b, c]

a = massiv_add[0] + massiv_add[1]
b = massiv_add[2] - massiv_add[0]
c = sum(massiv_add)

print("a =", a)
print("b =", b)
print("c =", c)"""

"""# 28
# Пользователь вводит сумму вклада в банк и годовой процент.
# Найдите сумму вклада через 5 лет (рассмотреть два способа начисления процентов)

a = float(input("Введите сумму вклада, грн "))
p = int(input("Введите годовой процент, % "))
s_1 = s_2 = a

for i in range(60):
    s_1 = s_1 + s_1 * p / (100 * 12)

for i in range(5):
    s_2 = s_2 + s_2 * p / 100

print("Сумма вклада за 5 лет при ежемесячном начислении процентов составит", s_1, "грн")
print("Сумма вклада за 5 лет при ежегодном начислении процентов составит", s_2, "грн")"""

"""# 29
# Поменяйте местами значения двух переменных, не используя дополнительных переменных.

x = 2
r = 3

x, r = r, x"""

"""# 30
# Дано число a. Не пользуясь никакими арифметическими операциями кроме умножения, получите 
# а)a4 за две операции; 
# б) a6 за три операции; 
# в) a15 за пять операций.

a = 4

a4 = 2 * 2 * a
a6 = 1 * 2 * 3 * a
a15 = 1 * 1 * 1 * 3 * 5 * a"""

"""# 31
# Дан прямоугольник размером 647 x 170. Сколько квадратов со стороной 30 можно вырезать из него?

x = 647
y = 170
b = 30

s = (x // b) * (y // b)
print("Количество квадратов со стороной 30 в указанном квадрате составит", s, "шт")
"""
"""# 32
# Из трехзначного числа x вычли его последнюю цифру. Когда результат разделили на 10,
# а к частному слева приписали последнюю цифру числа x, то получилось число 237. Найти число x.

s = "237"

finish_number = int(s[0])
prom_number = int(s[1:])
first_number = 10 * prom_number * 10 + finish_number

print(finish_number)
print(prom_number)
print("Начальное число равнялось =", first_number)"""

"""# 33

import math

x = float(input("Введите число X = "))
y = float(input("Введите число y = "))

z = x - math.sqrt(y)

if y > 0 and x ** 2 >= y:
    v = math.sqrt(z)
    print("Значение функции равно", v)
else:
    print("Уравнение не имеет решения")
"""
"""# 34
# Дано число. Если оно больше 3, то увеличить число на 10, иначе уменьшить на 10.

x = float(input("Введите число X = "))
if x > 3:
    x += 10
else:
    x -= 10
print("x=", x)"""

"""# 35
# Дано число. Если оно меньше 7, то вывести Yes, если больше 10, то вывести No, если равно 9, то вывести Error.

x = float(input("Введите число X = "))
if x < 7:
    print("Yes")
elif x > 10:
    print("No")
elif x == 9:
    print("Error")"""

"""#  36
# Пользователь вводит номер месяца, вывести название месяца.

months = {
    "1": "Январь",
    "2": "Февраль",
    "3": "Март",
    "4": "Апрель",
    "5": "Май",
    "6": "Июнь",
    "7": "Июль",
    "8": "Август",
    "9": "Сентябрь",
    "10": "Октябрь",
    "11": "Ноябрь",
    "12": "Декабрь",
}
number = int(input("Введите номер месяца: "))
if number in range(1, 13):
    print("Это месяц", months[str(number)])
else:
    print("Такого месяца нет")"""

"""# 37
# Дано два числа. Вывести наибольшее из них.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))

if x == y:
    print("x = y")
elif x > y:
    print("x > y")
else:
    print("x < y")"""
"""
# 38
# Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))

if abs(x - y) >= 100:
    print("Yes")
else:
    print("№")"""

"""# 39
# Даны два числа. Если первое число больше второго, то вывести yes, иначе поменять значения этих переменных
# и вывести их на экран.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))

if x > y:
    print("Yes")
else:
    x, y = y, x
    print("x = ", x, "y = ", y)"""

"""# 40
# Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, иначе уменьшить на 10.

x = float(input("Ввведите число x: "))

if abs(x) < 10:
    x += 5
    print("x = ", x)
else:
    x -= 10
    print("x = ", x)"""

"""# 41
# Дано число. Если оно более 100 или менее -100, то занулить, иначе увеличить его на 1.

x = float(input("Ввведите число x: "))

if abs(x) > 100:
    x = 0
    print("x =", x)
else:
    x += 1
    print("x =", x)"""

"""# 42
# Дано число. Если оно от 2 до 5 включительно, то увеличить его на 10. Если оно от 7 до 40, то уменьшить на 100.
# Если оно не более 0 или более 3000, то увеличить в 3 раза (то есть умножить на 3). Иначе занулить это число.

x = float(input("Ввведите число x: "))

if 2 <= x <= 5:
    x += 10
    print("x =", x)
elif 7 <= x <= 40:
    x -= 100
    print("x =", x)
elif x > 3000 or x <= 0:
    x *= 3
    print("x =", x)
else:
    x = 0
    print("x =", x)"""

"""# 43
# Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)

season = {
    "1": "Зима",
    "2": "Весна",
    "3": "Лето",
    "4": "Осень",
   }
number = float(input("Введите номер сезона: "))
if number % 2 == 0 or number % 2 == 1:
    if int(number) in range(1, 5):
        print("Это время года:", season[str(int(number))])
    else:
        print("Времени года с таким номером нет")
else:
    print("Времени года с таким номером нет")"""

"""# 44
# Пользователь вводит два числа. Если они не равны 10 и первое число четное,
# то вывести их сумму, иначе вывести их произведение.

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))

if x != 10 and y != 10 and x % 2 == 0:
    print("x + y =", x + y)
else:
    print("x * y =", x * y)"""

"""# 45
# Пользователь вводит три числа. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))

if x > 10 and y > 10 and z > 10 and x % 3 == 0 and y % 3 == 0:
    print("Yes")
else:
    print("No")"""

"""# 46
# Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5. Если таких чисел нет, то вывести error.

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))

c = [x, y, z]
summ_1 = 0

for i in range(len(c)):
    if c[i] % 5 == 0:
        summ_1 += c[i]
if summ_1 == 0:
    print("Error")
else:
    print("Сумма чисел равна", summ_1)"""

"""# 47
# Даны три числа. Найдите наибольшее число из них.

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))

if x > y and x > z:
    print("Наибольшее число х")
elif y > z:
    print("Наибольшее число y")
else:
    print("Наибольшее число z")"""

"""# 48
# Даны три числа. Найдите те два из них, сумма которых наибольшая.

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))

if x > z and y > z:
    summ_x_y = x + y
    print("Наибольшие числа х и y, x + y =", summ_x_y)
elif x > y and z > y:
    summ_x_z = x + z
    print("Наибольшие числа х и z, x + z =", summ_x_z)
else:
    summ_y_z = y + z
    print("Наибольшие числа y и z, y + z =", summ_y_z)"""

"""# 49
# Пользователь вводит четыре числа. Найдите наибольшее четное число среди них.
# Если оно не существует, выведите фразу "not found"

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))
w = int(input("Ввведите число w: "))

massiv_add = [x,y,z,w]
massiv_add.sort()

while massiv_add[3] % 2 != 0:
    massiv_add.insert(0, 0)
    massiv_add.pop()

massiv_add.sort()
if x % 2 == 0 and x == massiv_add[3]:
    print("Наибольшее число x =", x)
elif y % 2 == 0 and y == massiv_add[3]:
    print("Наибольшее число y =", y)
elif z % 2 == 0 and z == massiv_add[3]:
    print("Наибольшее число z =", z)
elif w % 2 == 0 and w == massiv_add[3]:
    print("Наибольшее число w =", w)
else:
    print("not found")"""

"""# 50
# Даны три числа. Написать "yes", если среди них есть одинаковые.

x = int(input("Ввведите число x: "))
y = int(input("Ввведите число y: "))
z = int(input("Ввведите число z: "))

w = [x, y, z]
w = list(set(w))
if len(w) < 3:
    print("Yes")"""

"""# 51
# Даны три числа. Написать "yes", если можно взять какие-то два из них и в сумме получить третье

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))
z = float(input("Ввведите число z: "))

if x + y == z or x + z == y or y + z == x:
    print("Yes")"""

"""# 52
# Дано четыре числа, если первые два числа больше 5, третье число делится на 6,
# четвертое число не делится на 3, то вывести yes, иначе no.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))
z = float(input("Ввведите число z: "))
w = float(input("Ввведите число w: "))

if x > 5 and y > 5 and z % 6 == 0 and w % 3 != 0:
    print("Yes")
else:
    print("No")"""

"""# 53
# Дано два числа. Если хотя бы одно из них больше 30, то вывести yes, иначе no.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))


if x > 30 or y > 30:
    print("Yes")
else:
    print("No")"""

"""# 54
# Дано три числа. Если ровно два из них  меньше 5, то вывести yes, иначе вывести no.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))
z = float(input("Ввведите число z: "))

if x < 5 and y < 5 and z < 5:
    print("No")
elif x < 5 and y < 5:
    print("Yes")
elif x < 5 and z < 5:
    print("Yes")
elif y < 5 and z < 5:
    print("Yes")
else:
    print("No")"""

"""# 55
# Дано три числа. Найти количество положительных чисел среди них.

x = float(input("Ввведите число x: "))
y = float(input("Ввведите число y: "))
z = float(input("Ввведите число z: "))

q = (x, y, z)
k = 0

for i in range(len(q)):
    if q[i] > 0:
        k += 1
print("Количество положительных чисел равно ", k)"""

"""# 56
# Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
# Дан число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
# Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).

run_robot = {
    11: "север",
    12: "запад",
    13: "юг",
    14: "восток",
    0: 0,
    1: 1,
    -1: -1,
    7: "Робот остановлен",
}

ex = 7

while x not in range(11, 15):
    x = int(input("Введите начальное положение робота (11 — север, 12 — запад, 13 — юг, 14 — восток): "))

print("Робот установлен в положение", '"' + str(run_robot[x]) + '"')

while y not in range(-1,3) or y != 2:
    y = int(input("Введите направдение движения робота (0 - продолжить движение, 1 - поворот налево, -1 - поворот направо, "
              "2 выход из режима управления роботом): "))
    if y == 2:
        continue
    else:
        x += y
        if x < 11:
            x = 14
            print("Робот установлен в положение", '"' + str(run_robot[x]) + '"')
        if x > 14:
            x = 11
            print("Робот установлен в положение", '"' + str(run_robot[x]) + '"')
        else:
            print("Робот установлен в положение", '"' + str(run_robot[x]) + '"')

print()
print("Ты решил закончить работу!")
print()
print("Удачи тебе! Возвращайся скорее!")
"""
"""# 57
# Дана дата из трех чисел (день, месяц и год). Вывести yes, если такая дата существует
# (например, 12 02 1999 - yes, 22 13 2001 - no). Считать, что в феврале всегда 28 дней.

data_input = input("Введите дату в следующем формате число.месяц.год: ")
f = data_input.split(".")
a = float(f[0])
b = float(f[1])
c = float(f[2])
print(a, b, c)
x = [1, 3, 5, 7, 8, 10, 12]
y = [4, 6, 9, 11]

if a in range(1, 32) and a % 1 == 0 and b in range(1, 13) and b % 1 == 0 and c in range(0, 2023) and c % 1 == 0:
    if b == 2:
        if a <= 28:
            print("Yes")
        else:
            print("No")
    elif b in x:
        if a <= 31:
            print("Yes")
        else:
            print("No")
    elif b in y:
        if a <= 30:
            print("Yes")
        else:
            print("No")
else:
    print("Mo")"""

"""# 58
# Дано две даты, каждая из которых состоит из трех чисел (день, месяц и год).
# Вывести yes, если первая дата раньше второй, иначе вывести no.

def chek_data(a, b, c):
    x = [1, 3, 5, 7, 8, 10, 12]
    y = [4, 6, 9, 11]
    z = 0

    if a in range(1, 32) and a % 1 == 0 and b in range(1, 13) and b % 1 == 0 and c in range(0, 2023) and c % 1 == 0:
        if b == 2:
            if a <= 28:
                z += 1
            else:
                z = 0
        elif b in x:
            if a <= 31:
                z += 1
            else:
                z = 0
        elif b in y:
            if a <= 30:
                z += 1
            else:
                z = 0
    else:
        z = 0
    return z


z_1 = 0
z_2 = 0
a_1 = 0
a_2 = 0
b_1 = 0
b_2 = 0
c_1 = 0
c_2 = 0

while z_1 == 0 or z_2 == 0:
    data_input_1 = input("Введите первую дату в следующем формате число.месяц.год: ")
    in_d1 = data_input_1.split(".")
    a_1 = float(in_d1[0])
    b_1 = float(in_d1[1])
    c_1 = float(in_d1[2])
    z_1 = chek_data(a_1, b_1, c_1)
    if z_1 == 0:
        print("Первой даты не существует, начните ввод заново")
        continue
    data_input_2 = input("Введите вторую дату в следующем формате число.месяц.год: ")
    in_d2 = data_input_2.split(".")
    a_2 = float(in_d2[0])
    b_2 = float(in_d2[1])
    c_2 = float(in_d2[2])
    z_2 = chek_data(a_2, b_2, c_2)
    if z_2 == 0:
        print("Второй даты не существует, начните ввод заново")
    print("z_1 =", z_1, "z_2 =", z_2)

if a_1 == a_2 and b_1 == b_2 and c_1 == c_2:
    print("Обе даты одинаковые")
elif c_1 != c_2 and c_1 > c_2:
    print("Первая дата больше второй")
elif b_1 != b_2 and b_1 > b_2:
    print("Первая дата больше второй")
elif a_1 != a_2 and a_1 > a_2:
    print("Первая дата больше второй")
else:
    print("Вторая дата больше первой")"""

"""# 59
# Дано четырехзначное число. Верно ли, что цифр в нем расположены по убыванию?
# Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.

def poisk(number):
    b = list(set(number))
    p = list(number)
    b.sort()
    b.reverse()
    if b == p:
        print("В числе цифры расположены по убыванию")
    else:
        print("В числе цифры НЕ расположены по убыванию")

a = input("Введите четырехзначное число: ")
poisk(a)"""

# 60
# Дано трехзначное число. Переставьте первую и последнюю цифры.


