# Написать программу, которая состоит из вечного цикла ожидающего ввод числа
# или одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать
# введённые числа. Сама функция ничего не распечатывает, она возвращает строку,
# типа: "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное
# число: Erdf". Затем в цикле выводится это сообщение и цикл начинается заново
# ожидая следующего ввода. Функция на вход принимает строку из ввода из вечного
# цикла. Анализирует её исключительно методом .isdigit() и другими методами
# строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же
# распознаёт десятичные дроби как с точкой, так и с запятой.
# Функция возвращает строку в которой описывается какое число ввеqдено -
# отрицательное или положительно, целое или дробное и выводит его или же
# сообщает, что введено не корректное число.
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля
#
# Примеры:
# -6,7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -.777 → Вы ввели отрицательное дробное число: -0.777


def check_string(input_number):
    # Ввод дополнительной переменной сокращает условие проверки. Какой иначе был бы код в if - внизу под комментами
    input_value = input_number.replace(",", '.')

    if len(input_number) == 0:
        string_out = "Вы ничего не ввели"

    # Определение как ноль строк: '0', '+0', '-0', '.000', ',000', '-.000', '+,000', '00,000', '00.000', '00000' и т.д.
    elif ((input_value.replace(".", '', 1)).isdigit() and float(input_value.replace(".", '', 1)) == 0) \
            or (input_value[0] in ("+", "-") and (input_value[1:].replace(".", '', 1).isdigit() and
                                                  float(input_value[1:].replace(".", '', 1)) == 0)):
        string_out = "Вы ввели:  0"

    elif input_value.isdigit() or (input_value[0] == "+" and input_value[1:].isdigit()):
        string_out = f"Вы ввели положительное целое число: {int(input_value)}"  # приведение формата +00005 к 5

    elif input_value[0] == "-" and input_value[1:].isdigit():
        string_out = f"Вы ввели отрицательное целое число: {int(input_value)}"  # приведение формата -00005 к -5

    # Проверка и определение как положительное дробное число строк: '0,1', '+0,1' '.001', '+,001', '000,001' '000.001',
    # '+000,0001', '+000.0001' и других
    elif (input_value.replace(".", '', 1)).isdigit() \
            or (input_value[0] == "+" and ((input_value[1:].replace(".", '', 1).isdigit()))):

        # float - выполнение исходного условия по выводу: "-.777 → Вы ввели отрицательное дробное число: -0.777"
        string_out = f"Вы ввели положительное дробное число: {float(input_value)}"

    # По аналогии с положительными дробными цифрами
    elif input_value[0] == "-" and (input_value[1:].replace(".", '', 1)).isdigit():
        string_out = f"Вы ввели отрицательное дробное число: {float(input_value)}"

    # вывод input_number,а не input_value, чтобы вывести именно введенное не верное число (с учетом ',')
    else:
        string_out = f"Вы ввели не корректное число: {input_number}"

    return string_out


while True:
    input_string = input("\nВведите любое число (для выхода введите - выход/exit/quit/e/q): ")
    print()
    input_string = input_string.strip()  # Обрезка по краям пробелов
    if input_string.lower() in ("выход", "exit", "quit", "e", "q"):
        print("До свидания!")
        break
    else:
        print(check_string(input_string))
    continue

"""def check_string(input_value):
    if len(input_value) == 0:
        string_out = "Вы ничего не ввели"

    elif ((input_value.replace(".", '', 1)).isdigit() and float(input_value.replace(".", '', 1)) == 0)\
        or ((input_value.replace(",", '', 1)).isdigit() and float(input_value.replace(",", '', 1)) == 0)\
        or (input_value[0] in ("+", "-") and ((input_value[1:].replace(".", '', 1).isdigit() and
        float(input_value[1:].replace(".", '', 1)) == 0) or (input_value[1:].replace(",", '', 1).isdigit() and
        float(input_value[1:].replace(",", '', 1)) == 0))):
        string_out = "Вы ввели:  0"

    elif input_value.isdigit() or (input_value[0] == "+" and input_value[1:].isdigit()):
        string_out = f"Вы ввели положительное целое число: {int(input_value)}" 

    elif input_value[0] == "-" and input_value[1:].isdigit():
        string_out = f"Вы ввели отрицательное целое число: {int(input_value)}"  

    elif (input_value.replace(".", '', 1)).isdigit() or (input_value.replace(",", '', 1)).isdigit()\
        or ((input_value[0] == "+" and ((input_value[1:].replace(".", '', 1).isdigit())
        or (input_value[1:].replace(",", '', 1)).isdigit()))):        
        input_value = input_value.replace(",", '.')
        string_out = f"Вы ввели положительное дробное число: {float(input_value)}"

    elif input_value[0] == "-" and ((input_value[1:].replace(".", '', 1)).isdigit()
        or (input_value[1:].replace(",", '', 1)).isdigit()):
        input_value = input_value.replace(",", '.')
        string_out = f"Вы ввели отрицательное дробное число: {float(input_value)}"

    else:
        string_out = f"Вы ввели не корректное число: {input_value}"

    return string_out


while True:
    input_number = input("\nВведите любое число (для выхода введите - выход/exit/quit/e/q): ")
    print()
    input_number = input_number.strip()
    if input_number.lower() in ("выход", "exit", "quit", "e", "q"):
        print("До свидания!")
        break
    else:
        print(check_string(input_number))
    continue
"""