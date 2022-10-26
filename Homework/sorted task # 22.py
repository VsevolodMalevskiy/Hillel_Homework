# Используя сортировку найдите три наименьших значения в спике. Сам список должен оставаться неизменным:


a = [1, 2, -5, 0.5, 10]
sort_min = sorted(a, reverse=False)[0:3]
print(sort_min)


# Отсортируйте список так, чтобы сначала шли отрицательные числа, а затем положительные:


digs = [-10, 0, 7, -2, 3, 6, -8]

digs_sort = sorted(digs, reverse=False)
print(digs_sort)

# Имеется словарь. Необходимо вывести телефонные номера по убыванию чисел, указанных в ключах. Т.е., +4, +5,  +7, +12


phone_number = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}

# var_1
phone_number_out1 = dict(sorted(phone_number.items(), key=lambda x: int(x[0][1:])))
# var_2
phone_number_out2 = {x: phone_number[x] for x in sorted(phone_number, key=lambda x: int(x))}
# phone_number_out2 = {x: phone_number[x] for x in sorted(phone_number, key=lambda x: int(x), reverse=True)}

print(phone_number_out1)
print(phone_number_out2)