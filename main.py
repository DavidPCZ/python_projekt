import graf
import tkinter
from tkinter import *
from tkinter import ttk
import python_project as pp

okno = Tk()
okno.geometry("1000x500")
buton = Frame(okno)

def dalsi():
      okno.destroy()
      pp.otazky()

Label(okno, text="Politický kompas", font=("Arial", 60)).pack()
Label(okno, text="Tento program za pomocí vašich odpovědí na otázky vypočítá, kde se na politickém kompasu nacházíte",
      font=("Arial", 15)).pack(expand=True, fill=BOTH)
Button(okno, text="Začít test", font=("Arial", 10), height=2, width=25, command=dalsi).pack()

mainloop()
# graf.kresgraf(5,5)
# samostatné zavolání funguje
