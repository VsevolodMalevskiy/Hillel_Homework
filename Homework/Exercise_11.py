# При помощи функции filter() из списка слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны),
# регистр букв не учитывать.


# Вариант 1. Усложнил условие - добавил проверку исходных данных в списке и сделал через внешнюю функцию

inputdata1 = ["Страна", "шалаш", "Летел", "вертолёт", "УЧУ", "мэм", "язык", 2333, {1: 23, 2: 34}, "222222222", "дОхоД",
           "father", "fDfdfdf", "fdfdf", "hghKKKhhh", "ЗАказ", "кабак", "казак", "saipPUakivikauppias", "Микрозорким",
           "Маревоверам"]


def filter_polindrom(string):
    if type(string) == str and string.isalpha() and string.lower() == (string[::-1]).lower():
        return True   # вместо True возможно возвращать string


list_out1 = list(filter(filter_polindrom, inputdata1))
print("\nВариант 1")
print(list_out1)


# Вариант 2. Без проверки исходных данных

inputdata2 = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
list_out2 = list(filter(lambda x: x.lower() == (x[::-1]).lower(), inputdata2))
print("\nВариант 2")
print(list_out2)
