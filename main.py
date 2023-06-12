import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def mainf(xvalue, yvalue):
    root = Toplevel()
    frm = ttk.Frame(root, padding=10)
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

    mainloop()

# mainf(5,5)
# samostatné zavolání funguje