import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def kresgraf(xvalue, yvalue):
    root = Tk()
    canvas = Canvas(root, width=930, height=807)
    canvas.pack()

    img = ImageTk.PhotoImage(Image.open("polcompass.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=img)

    xpos = (img.width() / 2 - 14)
    ypos = (img.height() / 2 + 1)

    # 36x36 velikost bloku kompasu
    # xhodnoty = 0
    # yhodnoty = 0

    dot = Image.open("dot.png")
    dotres = ImageTk.PhotoImage(dot.resize((25, 25)))  # 12 je ještě akceptovatelné v poměru velikost-přesnost
    canvas.create_image(xpos + (xvalue * 36), ypos - (xvalue * 36),
                        image=dotres)  # začátek střed, 1 v hodnotách je jeden blok

    nametext = tkinter.Label(root, text="Zadejte jméno")
    nametext.pack()

    nameentry = ttk.Entry(root)
    nameentry.pack()

    enter = tkinter.Button(root, text="Poslat", font=("Arial", 10), height=1, width=5)
    enter.pack()

    mainloop()
