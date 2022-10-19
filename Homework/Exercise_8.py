"""Дан список чисел.

Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.

Подсказка: для хранения данных использовать словарь (ключ - само число, а значение - сколько раз оно встречается).
Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in."""


# Три варианта решения

list_start = [12, 14, 17, 56, 34, 14, 19, 17, 17, 89, 90, 93, 98, 90]
list_start.sort()  # Для вывода в функции print отсортированного по ключям словаря


def fun_print(dict_sort):
    for key, value in dict_sort.items():
        print(f"Число - {key}, количество повторений - {value}")


# Вариант 1


def dictionary_count(list_in):
    dictionary_start = {}
    for item in list_in:
        if item in dictionary_start:
            dictionary_start[item] += 1
        else:
            dictionary_start[item] = 1
    return dictionary_start


print("\n#1 Вариант:")
fun_print(dictionary_count(list_start))

# Вариант 2


def dic_count(list_in):
    dictionary = {}
    for item in list_in:
        if dictionary.get(item, None):
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


print("\n#2 Вариант:")
fun_print(dic_count(list_start))

# Вариант 3

from collections import Counter   # необходимо располагать вначале кода, но импортировал здесь для варианта 3

dictionary_counter = Counter(list_start)
print("\n#3 Вариант:")
fun_print(dictionary_counter)
