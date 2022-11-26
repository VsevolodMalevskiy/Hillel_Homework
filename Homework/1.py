import re


def in_str(string):
    if string and string.isalpha():
        return string.isalpha()


def data_in(string):
    if string: # проверяет, что не пустая  строка
        return re.findall(r'\d{1,4}(?:-|.|/| )\d*(?:-|.|/| )\d{2,4}', str(string))

def sex_c(string):
    if string and string.isalpha() and string in ('муж', 'жен'):
        return True


# для фамилии
while True:
    in_f = input("Ввведите фамилию: ", )
    f_f = in_str(in_f)
    if f_f == True:
        break

#  для имени
while True:
    in_n = input("Ввведите имя: ", )
    f_n = in_str(in_n)
    if f_n == True or not in_n:  # not in_n проверяет на то, что ничего не введено, т.е. не обязательный ввод
        break

while True:
    in_o = input("Ввведите отчество: ", )
    f_o = in_str(in_o)
    if f_o == True or not in_o:  # not in_n проверяет на то, что ничего не введено, т.е. не обязательный ввод
        break


while True:
    in_db = input("Введите дату рождения: ", )
    f_db = data_in(in_db)
    if f_db:  # проверяет что из функции вернулась дата
        break


while True:
    in_dd = input("Введите дату смерти: ", )
    f_dd = data_in(in_dd)
    if f_dd or not in_dd:  # проверяет что из функции вернулась дата
        break

while True:
    in_s = input("Введите пол (муж, жен): ", )
    f_s = sex_c(in_s)
    if f_s:
        break



print("_" * 30)
print(in_f)
print(in_n)
print(in_o)
print(in_db)
print(in_dd)
print(in_s)










