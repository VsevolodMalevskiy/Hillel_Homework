# Функция разбивки строки по символам и создания списка, который будет использоваться для дальнейшей проверки строки.
# [0] - приинимает значение 0 или +1, если первый знак "+" и -1Б если первый знак"-"
# [1] - указывает на количество знаков "."
# [2] - указывает на количество цифр
def line_breaking(input_string):
    # Обнуление списка при каждом вызове функции
    check_array = [0, 0, 0]
    breakdown = list(input_string)
    if breakdown[0] == "+":
        check_array[0] = 1
    elif breakdown[0] == "-":
        check_array[0] = -1
    for item in breakdown[0+abs(check_array[0]):]:
        if item == "." and check_array[1] < 1:
            check_array[1] += 1
        elif item.isdigit():
            check_array[2] += 1
    print(check_array)
    return check_array


def check_string(list, second_value, first_string):
    # Проверка были ли в строке буквы или символы или более одного символа "."
    if len(second_value) != abs(list[0]) + list[1] + list[2] or list[1] > 1:
        inform_string = f"Вы ввели не корректное число: {first_string}"
    else:
        if float(input_value) == 0:
            inform_string = "Вы ввели:  0"
        elif list[1] == 0:
            if list[0] >= 0:
                inform_string = f"Вы ввели положительное целое число: {int(second_value)}"
            else:
                inform_string = f"Вы ввели отрцательное целое число: {int(second_value)}"
        elif list[0] >= 0:
            inform_string = f"Вы ввели положительное дробное целое число: {float(second_value)}"
        else:
            inform_string = f"Вы ввели отрицательное дробное целое число: {float(second_value)}"
    return inform_string


while True:
    input_string = input("\nВведите любое число (для выхода введите - выход/exit/quit/e/q): ")
    print()
    input_string = input_string.strip()
    if input_string.lower() in ("выход", "exit", "quit", "e", "q"):
        print("До свидания!")
        break
    else:
        if len(input_string) == 0:
            string_out = "Вы ничего не ввели"
        else:
            input_value = input_string.replace(",", '.')
            check_list = line_breaking(input_value)
            string_out = check_string(check_list, input_value, input_string)
    print(string_out)
