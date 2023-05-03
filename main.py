import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
frm = ttk.Frame(root, padding=10)
canvas = Canvas(root, width=930, height=807)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("polcompass.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

xpos = (img.width()/2 - 14)
ypos = (img.height()/2 + 1)

xhodnoty = 100
yhodnoty = 100

dot = Image.open("dot.png")
dotres = ImageTk.PhotoImage(dot.resize((8, 8)))
canvas.create_image(xpos + xhodnoty, ypos - yhodnoty, image=dotres)


mainloop()
