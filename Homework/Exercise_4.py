"""Написать программу которая получит имя и возраст пользователя, проверяет возраст и выдаёт приветственное сообщение
в зависимости от возраста:

- меньше нуля или ноль или не число: “Ошибка, повторите ввод”;

- больше нуля до 10 не включая: “Привет, шкет #Имя#”;

- от 10 до 18 включая: “Как жизнь #Имя#?”

- больше 18 и меньше 100: “Что желаете #Имя#?”

- в противном случае: “#Имя#, вы лжете - в наше время столько не живут...”

Программу необходимо завернуть в вечный цикл.

После очередной отработки кода, спрашивать у пользователя "Желаете выйти? (Д/Y)". Если ответ будет буква "Д"
или буква "Y" в любом регистре, то произвести выход из вечного цикла. В противном случае продолжить выполнение
программы заново."""


while True:
    input_name = input("Введите имя: ").strip()
    if not input_name.isalpha():
        print("Вы ввели не правильное имя! В веденном имени содержатся цифры или недопустимые знаки!")
        continue
    while True:
        input_age = input(f"{input_name.title()}, введите свой возраст: ").strip()
        if not input_age.isdigit() or int(input_age) <= 0:
            print("Ошибка, повторите ввод!")
            continue
        else:
            break

    input_name = input_name.title()
    input_age = int(input_age)

    if input_age < 10:
        print(f"Привет, шкет {input_name}!")
    elif input_age <= 18:
        print(f"Как жизнь, {input_name}?")
    elif input_age < 100:
        print(f"Что делаете, {input_name}?")
    else:
        print(f"{input_name}, вы лжете - в наше время столько не живут...")


    answer = input(f"{input_name}, хотите выйти? (Y/Д): ")
    if answer.title() in ("Y", "Д"):
        print(f"\n{input_name}, всего доброго!")
        break