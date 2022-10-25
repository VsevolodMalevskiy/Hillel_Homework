# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()

from datetime import datetime


def factor():
    while True:
        input_num = input("Введите целое положительное число > 0: ").strip()
        if not input_num.isdigit() or not int(input_num) > 0:
            print("Ошибка, повторите ввод!")
            continue
        else:
            input_num = int(input_num)
            break

    factorial = 1
    for item in range(1, input_num + 1):
        factorial *= item

    print(f"\n{input_num}! = {factorial}")
    return factorial


def filter_polindrom(*args: str):
    list_in = list(args)
    def filter_polin(string):
        if type(string) == str and string.isalpha() and string.lower() == (string[::-1]).lower():
            return string
    list_out = list(filter(filter_polin, list_in))
    print(f"\nСлова полиндромы {list_out}")


def time_test(fun):
    def wraper(*args):
        start_time = datetime.now()
        fun(*args)
        end_time = datetime.now() - start_time
        print(f"Затраченное время на выполнение функции = {end_time}")
    return wraper


time_1 = time_test(factor)
time_1()

time_2 = time_test(filter_polindrom)
time_2("", "ЭЭ4343434Э", "dfFD", "наВорован", "манекенаМ", "водоходов", "fgfgF", "1111")