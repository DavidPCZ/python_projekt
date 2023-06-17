import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def kresgraf(xvalue, yvalue):
    ratio = 0.9 # Ratio mění velikost dle procent (hodnota * 100%)
    root = Tk()
    canvas = Canvas(root, width=round(930*ratio), height=round(807*ratio))
    canvas.pack()

    img = Image.open("polcompass.jpg")
    img2 = ImageTk.PhotoImage(img.resize((round(930*ratio), round(807*ratio))))
    canvas.create_image(0, 0, anchor=NW, image=img2)

    xpos = (img2.width() / 2 - round(14*ratio))
    ypos = (img2.height() / 2 + round(1*ratio))

    # 36x36 velikost bloku kompasu
    # xhodnoty = 0
    # yhodnoty = 0

    dot = Image.open("dot.png")
    dotres = ImageTk.PhotoImage(dot.resize((round(25*ratio), round(25*ratio))))  # 12 je ještě akceptovatelné v poměru velikost-přesnost
    canvas.create_image(xpos + (xvalue * round(36*ratio)), ypos - (xvalue * round(36*ratio)),
                        image=dotres)  # začátek střed, 1 v hodnotách je jeden blok

    nametext = tkinter.Label(root, text="Zadejte jméno")
    nametext.pack()

    nameentry = ttk.Entry(root)
    nameentry.pack()

    enter = tkinter.Button(root, text="Poslat", font=("Arial", 10), height=1, width=5)
    enter.pack()

    mainloop()
