"""Сделать программу в виде функций в которой нужно будет угадывать число"""

import random

def input_name():
    while True:
        input_name = input("Привет! Как тебя зовут? ").strip()
        if not input_name.isalpha():
            print("Ты ввел не корректное имя, попробуй ввести еще раз!")
            continue
        else:
            break
    return input_name.title()

def start_welcom(name_w):
    print(f'{name_w}, давай поиграем в игру "Угадай число!"')
    print("Я загадал число от 1 до 30")
    print("У тебя 5 попыток, чтобы угадать число")

def input_number(name_n):
    while True:
        input_value = input(f"\n{name_n}, введи целое число от 1 до 30: ")
        if not input_value.isdigit() or not int(input_value) in range(31):
            print(f"\n{name_n}, ты ввел число не из диапазона от 1 до 30, попробуй ввести еще раз\n")
            continue
        else:
            return int(input_value)

def end_game(name_e):
    answer = input(f"{name_e}, хочешь закончить игру? (Y/Д): ")
    if answer.title() in ("Y", "Д"):
        print(f"\n{name_e}, всего доброго! Возвращайся скорей!")
        return False
    else:
        return True

name = input_name()
quit_game = True

while quit_game:
    start_welcom(name)
    attemps = 0
    number = random.randint(1, 30)
    while attemps < 5:

        input_numeric = input_number(name)

        if input_numeric < number:
            print(f"{name}, твое число меньше загаданного!")
        elif input_numeric > number:
            print(f"{name}, твое число больше загаданного!")
        elif input_numeric == number:
            print(f"{name}, ты угадал число! МОЛОДЕЦ!!!")
            break
        attemps += 1
        print(f"У тебя осталось {5 - attemps} попытки")
    else:
        print(f"{name}, ты проиграл!")

    quit_game = end_game(name)


