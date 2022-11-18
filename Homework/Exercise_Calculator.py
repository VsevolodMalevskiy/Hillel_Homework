# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.

# pyinstaller -F Homework\Exercise_Calculator.py

from tkinter import *
import math


root = Tk()
root.title('Калькулятор')
root.geometry("400x670")
# root.geometry("400x670+1450+300")

frm_form = Frame(relief=SUNKEN, borderwidth=3, height=1)
frm_form.pack()
ent_first_name = Entry(master=frm_form, font='arial 20', width=20, justify=RIGHT)  # show='*' скрывает под * ввод
ent_first_name.pack()

oper_massiv = {"/": 0, "*": 0, "+": 0, "-": 0, "%": 0}
check_key = {"key": 0}

def clear():
    ent_first_name.delete(len(ent_first_name.get())-1)   # удаление введенного текста


def clear_all():
    ent_first_name.delete('0', END)
    check_key["key"] = 0


def insert(meaning):
    ent_first_name.insert(len(ent_first_name.get()), meaning)


class Calculator:
    def __init__(self, argument):
        self.argument = float(argument)

    # 1/x
    def frac(self):
        return 1/self.argument

    # возведение в квадрат
    def exp(self):
        return self.argument**2

    # корень квадратный
    def sq(self):
        return math.sqrt(self.argument)

    # факториал
    def fact(self):
        num = 1
        for item in range(1, int(self.argument)+1):
            num *= item
        return num

    # деление
    def __truediv__(self, other):
        return self.argument/float(other)

    # умножение
    def __mul__(self, other):
        return self.argument * float(other)

    # сумма
    def __add__(self, other):
        return self.argument + float(other)

    # вычмтание
    def __sub__(self, other):
        return self.argument - float(other)

    # процент
    def __mod__(self, other):
        return self.argument * float(other)/100


x = Calculator("1")


def check_dig(in_str):
    return not in_str.replace(".", '', 1).isdigit() and in_str[0] != "-"


def check_neg(in_str):
    return not in_str[0] != "-"


def check_null(in_str):
    return float(in_str) == 0


def fraction():
    if not ent_first_name.get():
        return
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    elif check_null(x):
        return clear_all(), insert("division into 0")
    else:
        operator = Calculator(x)
        clear_all()
        insert(operator.frac())


# возведение в квадрат
def exponentiation():
    if not ent_first_name.get():
        return
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    elif check_null(x):
        return clear_all(), insert("division into 0")
    else:
        operator = Calculator(x)
        clear_all()
        insert(operator.exp())


# корень квадратный
def square():
    if not ent_first_name.get():
        return
    x = ent_first_name.get()
    if check_neg(x):
        return clear_all(), insert("negative square root")
    elif check_dig(x):
        return clear()
    else:
        operator = Calculator(x)
        clear_all()
        insert(operator.sq())


def factorial():
    if not ent_first_name.get():
        return
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    elif float(x) <= 0 or float(x) % 1 != 0:
        return clear_all(), insert("not factorial")
    else:
        operator = Calculator(x)
        clear_all()
        insert(operator.fact())


def minus():
    x = ent_first_name.get()
    if not x:
        return insert("-")
    elif len(x) == 1 and x[0] == "-":
        return clear_all()
    elif check_dig(x):
        return clear()
    elif float(x) < 0:
        x = x.replace("-", "")
        return clear_all(), insert(x)
    elif float(x) == 0:
        return
    else:
        return clear_all(), insert("-" + x)


def division():
    if oper_massiv["/"] != 0 or not ent_first_name.get():
        oper_massiv["/"] = 0
        return
    oper_massiv["/"] = 1
    print(oper_massiv)
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    else:
        global operator
        operator = Calculator(x)
        # clear_all()


def multiplication():
    if oper_massiv["*"] != 0 or not ent_first_name.get():
        oper_massiv["*"] = 0
        return
    oper_massiv["*"] = 1
    print(oper_massiv)
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    else:
        global operator
        operator = Calculator(x)
        # clear_all()


def addition():
    if oper_massiv["+"] != 0 or not ent_first_name.get():
        oper_massiv["+"] = 0
        return
    oper_massiv["+"] = 1
    print(oper_massiv)
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    else:
        global operator
        operator = Calculator(x)
        # clear_all()


def subtraction():
    if oper_massiv["-"] != 0 or not ent_first_name.get():
        oper_massiv["-"] = 0
        return
    oper_massiv["-"] = 1
    print(oper_massiv)
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    else:
        global operator
        operator = Calculator(x)
        # clear_all()


def percent():
    if oper_massiv["%"] != 0 or not ent_first_name.get():
        oper_massiv["%"] = 0
        return
    oper_massiv["%"] = 1
    print(oper_massiv)
    x = ent_first_name.get()
    if check_dig(x):
        return clear()
    elif float(x) < 0:
        return clear_all(), insert("not negative percents")
    else:
        global part_per
        part_per = operator % x
        clear_all()
        insert(part_per)


def equals():
    if sum(oper_massiv.values()) == 0:
        return
    if sum(oper_massiv.values()) == 2:
        y = str(part_per)
        oper_massiv["%"] = 0
    else:
        y = ent_first_name.get()
    if check_dig(y):
        return clear()
    elif oper_massiv["/"] == 1:
         if check_null(y):
             check_key["key"] = 0
             return clear_all(), insert("division into 0")
         else:
             oper_massiv["/"] = 0
             check_key["key"] = 0
             return clear_all(), insert(operator/y)
    elif oper_massiv["*"] == 1:
         oper_massiv["*"] = 0
         check_key["key"] = 0
         return clear_all(), insert(operator*y)
    elif oper_massiv["+"] == 1:
         oper_massiv["+"] = 0
         check_key["key"] = 0
         return clear_all(), insert(operator+y)
    elif oper_massiv["-"] == 1:
         oper_massiv["-"] = 0
         check_key["key"] = 0
         return clear_all(), insert(operator-y)



def clear_e(event):
    if sum(oper_massiv.values()) not in range(1, 2):
        return
    elif check_key["key"] == 0:
        clear_all()
        insert(event.keysym)
        check_key["key"] = 1
    else:
        return


# обработка вставки символа после нажатия оператора действия
def insert_num(clav):
    if sum(oper_massiv.values()) not in range(1, 2):
        return insert(clav)
    elif check_key["key"] == 0:
        clear_all()
        insert(clav)
        check_key["key"] = 1
    else:
        return insert(clav)


def num_0():
    insert_num("0")


def num_1():
    insert_num("1")

def num_2():
    insert_num("2")

def num_3():
    insert_num("3")

def num_4():
    insert_num("4")

def num_5():
    insert_num("5")

def num_6():
    insert_num("6")

def num_7():
    insert_num("7")

def num_8():
    insert_num("8")

def num_9():
    insert_num("9")

def num_point():
    insert_num(".")


d = {0: percent, 1: clear_all, 2: clear, 3: factorial, 4: fraction, 5: exponentiation,
     6: square, 7: division, 8: num_7, 9: num_8, 10: num_9, 11: multiplication,
     12: num_4, 13: num_5, 14: num_6, 15: subtraction, 16: num_1, 17: num_2,
     18: num_3, 19: addition, 20: minus, 21: num_0, 22: num_point, 23: equals}

but_list = ["%", "C", "del", "X!",
           "1/x", "X"+chr(178),
            chr(8730)+"X", "/",
             "7", "8", "9", "*",
             "4", "5", "6", "-",
             "1", "2", "3", "+",
           "+/-", "0", ",", "="]

axis_x = 10
axis_y = 100
for key, num in enumerate(but_list):
    button = Button(root, command=d[key], text=but_list[key], width=7, height=3, bg='white',
                    fg='red' if num in ["C", "del", "="] else 'black', font='arial 14')
    button = button.place(x=axis_x, y=axis_y)
    axis_x += 98
    if (key + 1) % 4 == 0:
        axis_y += 95
        axis_x = 10


def del_error(tab):
    z = ent_first_name.get()
    if z[-1] != tab:
        check_key["key"] = 1
        clear_all()
        insert(z)
        addition()
    else:
        clear_all()
        insert(z[:-1])
        addition()


def equals_e(eveny):
    equals()

def division_e(event):
    del_error("/")

def multiplication_e(event):
    del_error("*")

def subtraction_e(event):
    del_error("-")

def addition_e(event):
    del_error("+")


def clear_e(event):
    if sum(oper_massiv.values()) not in range(1, 2):
        return
    elif check_key["key"] == 0:
        clear_all()
        insert(event.keysym)
        check_key["key"] = 1
    else:
        return


root.bind('<Return>', equals_e) # клавиша "Enter"
root.bind('/', division_e)
root.bind('*', multiplication_e)
root.bind('-', subtraction_e)
root.bind('+', addition_e)
root.bind('<Key>', clear_e)

root.mainloop()


