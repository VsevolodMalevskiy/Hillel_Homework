from tkinter import *

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

    def intr(self):
        self.entry.pack()

    def get(self):
        return self.entry




    def ent(self):
        Label(text=self.title_in, width=0, height=3).pack()
        frm_first = Frame(relief=SUNKEN, borderwidth=3, height=1)
        frm_first.pack()
        self.Entry(master=frm_first, font='arial 12', width=30, justify=RIGHT).pack()


