# Написать программу для работы с данными о людях.
# Программа должна уметь загружать данные из файла, сохранять в файл, вводить новые записи и производить поиск
# по существующим записям.
# Программа сохраняет данные о человеке, а именно: ФИО, дата рождения, дата смерти (может отсутствовать) и пол.
# При этом ФИО вводится 3 полями: Имя (обязательно), Фамилия и Отчество могут не вводится.
# Программа должна уметь вычислять возраст человека (количество полных лет) на основании даты рождения и
# даты смерти или сегодняшней даты, если дата смерти отсутствует.
# Дата рождения и дата смерти может вводится в формате:
# 12.10.1980
# 11 10 2000
# 01/02/1995
# 3-9-2007
# Поиск может производится по имени, фамилии и отчеству и выдаёт все варианты, которые подходят под строку поиска
# (это может быть имя, или фамилия, или имя и фамилия, или только часть имени и т.д.).
# К примеру, есть такие записи:
# Евгений Крут Михайлович, 12.10.1980, 11.10.2001, m
# Евгения, 12.10.1980, 12.10.2001, f
# Дмитрий Евгеньевич, 10.03.2000, m
# При поиске "евген", выдаются такие данные:
# Евгений Крут Михайлович  20 лет, мужчина. Родился: 12.10.1980. Умер: 11.10.2001.
# Евгения 21 год, женщина. Родилась: 12.10.1980. Умерла: 12.10.2001.
# Дмитрий Евгеньевич 22 года, мужчина. Родился: 10.03.2000.
# Программа при старте начинает работать с пустой базой данных. Оператор может заполнять её, а может при желании
# загрузить ранее сохранённые данные из файла (желательно Excel).
#
# Когда есть какие-то записи оператор может сохранить их в файл введя его название.

# Желательная структура программы:

# в основной части программы находится вечный цикл с меню, что может выбрать оператор;
# сами данные организованы в виде класса в другом файле, который импортируется в файл основной части программы,
# где создаётся объект соответствующего класса перед заходом в вечный цикл;
# все пункты меню основной части программы вызывают те или иные методы у созданного объекта данных;
# при желании можно в третьем файле создать отдельный класс Person который будет импортироваться в файл с данными.
# Именно в этом классе будет происходить валидация введённых данных.
#
#
# *Все перечисленные описания являются пожеланиями по реализации дипломного проекта и в силу тех или иных причин
# могут быть изменены по желанию студента. Основные требования:
#
# программа позволяет ввести новые данные о людях;
# производить поиск по уже введённым данным;
# правильно рассчитывать количество полных лет человека на основе даты рождения и даты смерти или текущей даты.


import sqlite3 as sq
import time

from functions import *
from fun_tkinter import *
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox as mb
import math
import re
import os
import sys
import os.path


root = Tk()
root.title('Жильцы микрорайона Победа')
root.resizable = (False, False) # запрет на изменение размеров окна
root.geometry("400x670+1400+350")


ent_last_name = Entry_in("Фамилия*")
ent_first_name = Entry_in("Имя")
ent_patr = Entry_in("Отчество")
ent_date_birth = Entry_in("Дата рождения*")
ent_date_death = Entry_in("Дата смерти")
ent_sex = Entry_in("Пол* (муж*, жен*, f*, m*)")
ent_search = Entry_in("Поиск")
save_file = File_xlsx()


def file_save():
    try:
        path_file = File_xlsx()
        path = path_file.choose_file()
        amount = insert_in_db(path)
        win = win_inform()
        win.show_warning_1(amount)
    except:
        x_t = win_inform()
        x_t.show_warning("Не удалось сохранить данные из файла")


def db_inpanel():
    panel_massiv = []
    in_l = ent_last_name.input_panel().get()
    in_f = ent_first_name.input_panel().get()
    in_p = ent_patr.input_panel().get()
    in_b = ent_date_birth.input_panel().get()
    in_d = ent_date_death.input_panel().get()
    in_s = ent_sex.input_panel().get()
    if in_l and in_b and in_s:
        in_l = check_string(in_l)
        in_f = check_string(in_f)
        in_p = check_string(in_p)
        in_b = re.findall(KEY_DATA, in_b)
        if in_b:
            in_b = convert_data(in_b[0])
        in_d = re.findall(KEY_DATA, in_d)
        if in_d:
            in_d = convert_data(in_d[0])
        if in_d and in_b and in_b > in_d:
            in_b = None
            x_t = win_inform()
            x_t.show_warning("Дата смерти раньше даты рождения")
            ent_date_birth.input_panel().delete('0', END)
            ent_date_death.input_panel().delete('0', END)
        if in_s:
            in_s = check_sex(in_s)
        if in_l and in_b and in_s:
            if not in_f:
                in_f = None
            if not in_p:
                in_p = None
            if not in_d:
                in_d = None
            panel_massiv.append((in_l, in_f, in_p, in_b, in_d, in_s))
            add_file_db(panel_massiv)

            ent_last_name.input_panel().delete('0', END)
            ent_first_name.input_panel().delete('0', END)
            ent_patr.input_panel().delete('0', END)
            ent_date_birth.input_panel().delete('0', END)
            ent_date_death.input_panel().delete('0', END)
            ent_sex.input_panel().delete('0', END)
            x_t = win_inform()
            x_t.show_warning("Данные загружены в БД")
        else:
            x_t = win_inform()
            x_t.show_warning("Не заполнены все поля или формат ввода не корректный")
    else:
        x_t = win_inform()
        x_t.show_warning("Не заполнены все поля или формат ввода не корректный")


# def convert_data(data):
#     data_c = data[8:]+data[4:8]+data[:4]
#     return data_c
#
#
# def preparation(list_pr):
#     out_1 = list_pr[1].title()
#     if list_pr[2]:
#         out_2 = list_pr[2].title()
#     else:
#         out_2 = ''
#     if list_pr[3]:
#         out_3 = list_pr[3].title()
#     else:
#         out_3 = ''
#     out_4 = convert_data(list_pr[4])
#     if list_pr[5]:
#         out_5 = convert_data(list_pr[5])
#         age = int(out_5[6:]) - int(out_4[6:])
#         if int(out_5[3:5]) < int(out_4[3:5]):
#             age -= 1
#         elif int(out_5[3:5]) == int(out_4[3:5]) and int(out_5[:2]) < int(out_4[:2]):
#             age -= 1
#     else:
#         out_5 = ''
#         d_t = datetime.date.today()
#         age = int(d_t.year) - int(out_4[6:])
#         if int(d_t.month) < int(out_4[3:5]):
#             age -= 1
#         elif int(d_t.month) == int(out_4[3:5]) and int(d_t.day) < int(out_4[:2]):
#             age -= 1
#     out_6 = list_pr[6]
#     if int(str(age)[-1]) == 1:
#         let = 'год'
#     elif int(str(age)[-1]) in [2, 3, 4]:
#         let = 'года'
#     else:
#         let = 'лет'
#
#     if out_6 == 'мужчина':
#         rod = 'Родился'
#         mer = "Умер"
#     else:
#         rod = "Родилась"
#         mer = 'Умерла'
#     if not out_5:
#         mer = ''
#
#     l_pr = f"{out_1} {out_2} {out_3} {age} {let}, {out_6}. {rod} {out_4}. {mer} {out_5}"
#     return l_pr


def search_persons():
    in_search = ent_search.input_panel().get()
    if in_search:
        search_list = db_check_out(in_search)
        if not search_list:
            x_t = win_inform()
            x_t.show_warning("Записи в БД не найдены")
        else:
            with open("reviev.txt", "w") as file_txt:
                for string in search_list:
                    print(preparation(string), file=file_txt)
            file_txt.close()
            path_txt = os.path.join(sys.path[0], "reviev.txt")
            os.startfile(path_txt)



btn_1 = Button_p(150, 610, db_inpanel, "Ok")
btn_2 = Button_p(20, 610, file_save, "Save .xlsx")
btn_3 = Button_p(280, 610, search_persons, "Search")



# s = insert_in_db('Жители района.xlsx')
# print("Загружено строк из файла .xlsx:", s)


# c = db_check_out('из')
# print(len(c), c)

root.mainloop()
