from tkinter import *
import tkinter.messagebox as mb
import tkinter.filedialog as fd


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

    def show_warning_3(self, n):
        msg = f"Добавлено записей в файл: {n}"
        mb.showwarning("Предупреждение", msg)



    def show_error(self):
        msg = "Приложение обнаружило неизвестную ошибку"
        mb.showerror("Ошибка", msg)


class File_xlsx():
    def __init__(self):
        self.btn_file = Button(text="Выбрать файл", command=self.choose_file)
        self.btn_dir = Button(text="Выбрать папку", command=self.choose_directory)
        # self.btn_file.pack(padx=60, pady=10)
        # self.btn_dir.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("База данных", "*.xlsx"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            return filename

    def choose_directory(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            print(directory)
