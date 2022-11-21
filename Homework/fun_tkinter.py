from tkinter import *
import tkinter.messagebox as mb

# def win_enter(title_in, x):
#     Label(text=title_in, width=0, height=3).pack()
#     frm_first = Frame(relief=SUNKEN, borderwidth=3, height=1)
#     frm_first.pack()
#     x = Entry(master=frm_first, font='arial 12', width=30, justify=RIGHT).pack()


class Entry_in():

    def __init__(self, title_in):
        self.title_in = title_in
        self.label = Label(text=self.title_in, width=0, height=3)
        self.label.pack()
        self.frm = Frame(relief=SUNKEN, borderwidth=3, height=1)
        self.frm.pack()
        self.entry = Entry(master=self.frm, font='arial 12', width=30, justify=RIGHT)
        self.entry.pack()

    def input_panel(self):
        return self.entry


class win_inform():
    def __init__(self):
        self.btn_info = Button(text="Информационное окно")
        self.btn_warn = Button(text="Окно с предупреждением")
        self.btn_error = Button(text="Окно с ошибкой")

    def show_info(self):
        msg = "Ваши настройки сохранены"
        mb.showinfo("Информация", msg)

    def show_warning_1(self):
        msg = "Не заполнены все поля или формат ввода не корректный"
        mb.showwarning("Предупреждение", msg)

    def show_warning_2(self):
        msg = "Дата смерти раньше даты рождения"
        mb.showwarning("Предупреждение", msg)

    def show_error(self):
        msg = "Приложение обнаружило неизвестную ошибку"
        mb.showerror("Ошибка", msg)



