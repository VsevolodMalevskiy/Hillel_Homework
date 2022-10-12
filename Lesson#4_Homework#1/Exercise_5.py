"""Ввести с клавиатуры целое число n.

Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.

Реализовать в 2-х вариантах: используя цикл while и цикл for"""

# запрос и проверка введенного значения

cycle_breaker = True
input_value = 0

while cycle_breaker:
    input_value = input("Введите целое число больше 0: ")
    if not input_value.isdigit() or int(input_value) <= 0:
        print("Введено не корректное число, введите повторно\n")
        continue
    else:
        input_value = int(input_value)
        cycle_breaker = False
print()

# решение с циклом wnile

operand = 1
value_cube = 0

while operand <= input_value:
    if operand % 3 == 0:
        operand += 1
    else:
        value_cube += operand ** 3
        operand += 1

print("# цикл while")
print(f"Cумма кубов всех целых чисел от 1 до {input_value}, за исключением кратных трем = {value_cube}\n")



# решение с циклом for

value_cube2 = 0

for item in range(input_value + 1):
    if item % 3 == 0:
        item += 1
    else:
        value_cube2 += item ** 3
        item += 1

print("# цикл for")
print(f"Cумма кубов всех целых чисел от 1 до {input_value}, за исключением кратных трем = {value_cube2}")
