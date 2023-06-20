import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pyexcel as pe
import python_project
import getdotaz_new


def kresgraf(xvalue, yvalue):
    def zaznamenej(nametext, xvalue, yvalue):
        try:
            sheet = pe.get_sheet(file_name="data.ods")
        except:
            pe.save_as(array=[["Jméno", "OsaX", "OsaY"]], dest_file_name="data.ods")
            sheet = pe.get_sheet(file_name="data.ods")

        data = [str(nametext), xvalue, yvalue]

        sheet.row += data
        sheet.save_as("data.ods")

        messagebox.showinfo(message="Data byla uložena do souboru data.ods ve složce projektu")
        root.destroy()

    ratio = 0.85  # Ratio mění velikost dle procent (hodnota * 100%)
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
    canvas.create_image(xpos + (xvalue * round(36*ratio)), ypos - (yvalue * round(36*ratio)),
                        image=dotres)  # začátek střed, 1 v hodnotách je jeden blok

    strany = ["KSČM", "SocDem", "Zelení", "Piráti", "KDU-ČSL", "ANO", "STAN", "TOP 09", "ODS", "SPD", "Trikolóra", "Svobodní" ]
    souradnice = [[-7,6],[-5, -2],[-2,-5],[-1,-6],[1,5],[2,4],[2,-3],[5,-2],[6,3],[3,6],[6,5],[7,2]]    
    
    min_rozdil = 100
    min_rozdil_strana = ""
    for i in range(len(strany)):
        aktualnix = souradnice[i][0]
        aktualniy = souradnice[i][1]
                
        #print(aktualnix)
        #print(aktualniy)
                
        rozdil_x = abs(xvalue - aktualnix)
        rozdil_y = abs(yvalue - aktualniy)
        rozdil_celkem = rozdil_x + rozdil_y
    
        if(rozdil_celkem < min_rozdil):
            min_rozdil = rozdil_celkem
            min_rozdil_strana = strany[i]
    
            #print(min_rozdil, min_rozdil_strana)

    nejblizsi_strana = tkinter.Label(root, text="Vaše nejbližší strana: " + min_rozdil_strana)
    nejblizsi_strana.pack()

    nametext = tkinter.Label(root, text="Zadejte jméno")
    nametext.pack()

    nameentry = ttk.Entry(root)
    nameentry.pack()

    enter = tkinter.Button(root, text="Poslat", font=("Arial", 10), height=1, width=5, command=lambda: zaznamenej(nameentry.get(), xvalue, yvalue) )
    enter.pack()

    mainloop()
