"""Написать лямбда-функцию определяющую чётное/нечётное.

Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”, если нет - то “не чётное”."""

# Принимается, что 0 яляется четным числом и отрицательные числа так же могут делиться на четные или не четные


def in_number():
    while True:
        input_number = input("Введите целое число: ").strip()
        if not (input_number.strip("-")).isdigit():             # принимаются так же отрицательные числа
            print("Ошибка, повторите ввод!")
            continue
        else:
            break
    return int(input_number)


number = lambda x: "четное" if x % 2 == 0 else "не четное"

while True:
    input_num = in_number()             # Ввел дополнительную переменную, чтобы вывести в print введенное число
    check_number = number(input_num)
    print(f"Введенное число {input_num} {check_number}")
    answer = input("Хотите продолжить? (Y/Д): ")
    if answer.title() not in ("Y", "Д"):
        print("Всего доброго!")
        break

