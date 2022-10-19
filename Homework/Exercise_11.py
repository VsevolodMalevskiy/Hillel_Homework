# При помощи функции filter() из списка слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны),
# регистр букв не учитывать.


# несколько усложнил исходный список для тренировки проверки исходных данных

list_in = [2333, {1: 23, 2: 34}, "222222222", "дОхоД", "father","fDfdfdf", "fdfdf", "hghKKKhhh", "ЗАказ", "кабак",
           "казак", "saipPUakivikauppias","Микрозорким", "Маревоверам"]

def filter_polindrom(string):
    if type(string) == str and string.isalpha() and string.lower() == (string[::-1]).lower():
        return True


list_out = list(filter(filter_polindrom, list_in))
print(list_out)