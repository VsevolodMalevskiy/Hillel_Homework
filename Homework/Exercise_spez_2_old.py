# Написать программу для поиска файлов и построкового сравнения двух файлов.
# 1. Если код запустить с 2 аргументами, то каждым аргументом должно быть либо
# название файла, либо название файла с путём к нему, например:
# python homework\exercise_spez_2.py -a homework\1.txt -s 2.txt
# Данный вызов построково сравнивает текстовый файл test1.txt, который
# находится по тому же пути, что и запускаемый скрипт с текстовым файлом
# test2.txt который находится по пути: c:\temp\
# 2. Код можно запустить с ключами -f, -t и -d.
# а) Если код запускается с ключём -f то после него указывается шаблоном по
# которому в текущей директории и во всех поддиректориях будут искаться файлы.
# При этом если в имени использовать знак * - это означает любое количество любых
# символов, а знак ? - любой один символ. Пример:
# python exercise_spez_2.py -f "*.txt"
# Данный вызов находит все файлы с расширением txt в текущей директории и всех
# поддиреториях.
# б) Скрипт можно запустить одновременно с ключом -f и ключом -t с любым текстом
# после него (если текст отделён пробелами, то его необходимо брать в кавычки).
# В этом случае будут найдены только те файлы которые соответствуют шаблону
# поиска, а так же в этих файлах должен быть указанный текст. Пример:
# python exercise_spez_2.py -f "*.txt" -t "искомый текст"
# Данный вызов находит все файлы с расширением txt в текущей директории в которых
# есть текст "искомый текст".
# в) Так же скрипт можно запустить одновременно с ключом -f и ключом -d, после
# которого необходимо указать путь директории в которой будет осуществляться поиск
# файлов по заданному шаблону, а так же во всех её поддиректориях. Пример:
# python exercise_spez_2.py -f "*.txt" -d "c:\user\main"
# В этом случае файлы по шаблону *.txt будут искаться в директории по пути
# c:\user\main, а так же по всех её поддиректориях.
# Если после ключа -d указать знак "/", то поиск по заданному файлов шаблону
# будет осуществляться только в текущей диретории. Пример:
# python exercise_spez_2.py -f "*.txt" -d \
# Таким образом значение ключ -f всегда обязателен для поиска, а вот ключи -t и -d,
# при этом они могут использоваться как по одному, так и вместе в одном запросе:
# python exercise_spez_2.py -f "*.txt" -t "искомый текст" -d \
# Чтение ключей необходимо сделать при помощи библиотеки (argparse).
# Описание библиотеки os:
# https://pythonworld.ru/moduli/modul-os.html
# https://pythonworld.ru/moduli/modul-os-path.html

# 1. python homework\exercise_spez_2.py -f '?.txt' -d 'c:\temp'
# 2. python homework\exercise_spez_2.py -a homework\1.txt -s 2.txt
# 3. python homework\exercise_spez_2.py -f '?.txt' -t 'храниться до 2 лет' -d 'c:\temp'

import os
import os.path
import sys
import argparse
import fnmatch
import copy


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='--text', type=str, help='Needed text in file')
    parser.add_argument('-f', metavar='--file', type=str, help='Pattern of finding file')
    parser.add_argument('-d', metavar='--directory', type=str, help='Start directory to find')

    return parser.parse_args()


# Проверка отличий в строках двух файлов
def check_file(parser_a, parser_s):
    print()
    analyzed_file = open(parser_a, 'r', encoding='UTF-8')
    sample_file = open(os.path.join("C:/Temp", parser_s), 'r', encoding='UTF-8')
    line_count_analyzed = sum(1 for line in analyzed_file)
    line_count_sample = sum(1 for line in sample_file)
    analyzed_file.seek(0)
    sample_file.seek(0)

    for item in range(max(line_count_analyzed, line_count_sample)):
        x_string = copy.copy(analyzed_file.readline())
        y_string = copy.copy(sample_file.readline())
        if x_string != y_string:
            print(f"Строка {item + 1}  {x_string} \n {' '*10}{y_string}")
    print()
    analyzed_file.close()
    sample_file.close()


# Поиск фалов по шаблону и дирректории
def searched_file(file_search, directory):
    list_path = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in fnmatch.filter(files, file_search):
                list_path.append((file, os.path.join(root, file)))
    return list_path


#Поиск текстов в фалах
def search_text(list_file, text):
    list_coincidence = []
    for item in range(len(list_file)):
        file = open(list_file[item][1], 'r', encoding="UTF-8")
        if text in file.read():
            list_coincidence.append(list_file[item])
        file.close()
    return list_coincidence


# Основной блок

if len(sys.argv) == 3 and sys.argv[1][0] != '-' and sys.argv[2][0] != '-' and os.path.isfile(sys.argv[1])\
    and os.path.isfile(os.path.join("C:/Temp", sys.argv[2])):
    key_a = sys.argv[1]
    key_s = sys.argv[2]
    check_file(key_a, key_s)
else:
    parser = create_parser()
    if parser.f:
        # запуск поиска файлов и по дирректориям
        directory = os.getcwd() if not parser.d else parser.d
        path_file = searched_file(parser.f, directory)
        # запуск поиска текста в найденых файлах по шаблону
        if parser.t and len(path_file) != 0:
            if len(path_file) == 0:
                print("Совпадений не найдено")
            else:
                check_out = search_text(path_file, parser.t)
                if len(check_out) != 0:
                    for item in range(len(check_out)):
                        print(f"Найдены совпадения в файле: {check_out[item][0]},   путь: {check_out[item][1]}")
                else:
                    print("Совпадений не найдено")
        if len(path_file) != 0 and not parser.t:
            for item in range(len(path_file)):
                print(f"Найден файл: {path_file[item][0]},     расположение: {path_file[item][1]}")
        elif not parser.t:
            print("Файл не найден")



# 1. python homework\exercise_spez_2_old.py -f '?.txt' -d 'c:\temp'
# 2. python homework\exercise_spez_2_old.py homework\1.txt 2.txt
# 3. python homework\exercise_spez_2_old.py -f '?.txt' -t 'храниться до 2 лет' -d 'c:\temp'