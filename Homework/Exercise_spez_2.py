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

import os
import os.path
import argparse
import fnmatch
import copy


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', metavar='--file', type=str, help='Parsed file')
    parser.add_argument('-s', metavar='--file', type=str, help='Template file')
    parser.add_argument('-t', metavar='--text', type=str, help='Needed text in file')
    parser.add_argument('-f', metavar='--file', type=str, help='Pattern of finding file')
    parser.add_argument('-d', metavar='--directory', type=str, help='Start directory to find')

    return parser.parse_args()


def check_file():
    print()
    analyzed_file = open(parser.a, 'r', encoding='UTF-8')
    sample_file = open(os.path.join("C:/Temp", parser.s), 'r', encoding='UTF-8')
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


def searched_file(file_search, directory):
    list_path = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in fnmatch.filter(files, file_search):
                list_path.append((file, os.path.join(root, file)))
    return list_path


def search_text(list_file, text):
    list_coincidence = []
    for item in range(len(list_file)):
        file = open(list_file[item][1], 'r', encoding="UTF-8")
        if text in file.read():
            list_coincidence.append(list_file[item])
        file.close()
    return list_coincidence


parser = create_parser()

if parser.a and parser.s and os.path.isfile(parser.a) and os.path.isfile(os.path.join("C:/Temp", parser.s)):
    check_file()


if parser.f:
    directory = os.getcwd() if not parser.d else parser.d
    path_file = searched_file(parser.f, directory)
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



# python homework\exercise_spez_2.py -f '?.txt' -d 'c:\temp'
# python homework\exercise_spez_2.py -a homework\1.txt -s 2.txt
# python homework\exercise_spez_2.py -f '?.txt' -t 'храниться до 2 лет' -d 'c:\temp'