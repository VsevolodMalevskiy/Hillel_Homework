# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.


string_in1 = input("Введите первую строку: ")
string_in2 = input("Введите вторую строку: ")
string_in3 = input("Введите третью строку: ")
string_in4 = input("Введите четвертую строку: ")

file_txt = open('test_file.txt', 'w')

try:
    file_txt.writelines([string_in1 + "\n", string_in2 + "\n"])
finally:
    file_txt.close()

file_txt = open('test_file.txt', 'a+')

try:
    file_txt.writelines([string_in3 + "\n", string_in4])
    file_txt.seek(0)
    print(file_txt.read())
finally:
    file_txt.close()
