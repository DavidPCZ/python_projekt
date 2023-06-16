import tkinter as tk
import getdotaz_new
import graf

id_otazky = 1

xvalue = 0
yvalue = 0

def otazky():
    window = tk.Tk()
    window.geometry("1000x500")

    label_id = tk.Label(window, text=id_otazky, font=("Arial", 90))
    label_id.pack(expand=True, fill=tk.BOTH)

    button_frame = tk.Frame(window)
    text_size = 10

    def setvalue(vaha):
        global xvalue
        global yvalue
        global id_otazky

        smer = getdotaz_new.getdotazf(id_otazky, 2)

        if smer == "X":
            xvalue += getdotaz_new.getdotazf(id_otazky, 3) * vaha
        elif smer == "Y":
            yvalue += getdotaz_new.getdotazf(id_otazky, 3) * vaha

        print("id otázky:", id_otazky)
        print("xvalue:", xvalue)
        print("yvalue:", yvalue)
        # print("dotaz: ", dotaz)
        # print("smer: ", smer)
        # print("----")

        id_otazky += 1

        # if(id_otazky == )

        dotaz = getdotaz_new.getdotazf(id_otazky, 1)

        label_id.config(text=id_otazky)
        label_dotaz.config(text=dotaz)

        if (id_otazky == getdotaz_new.pocet_otazek):
            window.destroy()
            graf.kresgraf(xvalue, yvalue)

    smer = " "
    button1 = tk.Button(button_frame, text="Určitě souhlasím", font=("Arial", text_size), height=2, width=25,
                        command=lambda: setvalue(1))
    button2 = tk.Button(button_frame, text="Spíše souhlasím", font=("Arial", text_size), height=2, width=25,
                        command=lambda: setvalue(0.5))
    button3 = tk.Button(button_frame, text="Nevím / nedokážu odpovědět", font=("Arial", text_size), height=2, width=25,
                        command=lambda: setvalue(0))
    button4 = tk.Button(button_frame, text="Spíše nesouhlasím", font=("Arial", text_size), height=2, width=25,
                        command=lambda: setvalue(-0.5))
    button5 = tk.Button(button_frame, text="Určitě nesouhlasím", font=("Arial", text_size), height=2, width=25,
                        command=lambda: setvalue(-1))

    button1.pack(side="left", padx=5, pady=5)
    button2.pack(side="left", padx=5, pady=5)
    button3.pack(side="left", padx=5, pady=5)
    button4.pack(side="left", padx=5, pady=5)
    button5.pack(side="left", padx=5, pady=5)

    label_dotaz = tk.Label(window, text=getdotaz_new.getdotazf(id_otazky, 1), font=("Arial", 18))
    label_dotaz.pack(pady=10)
    button_frame.pack(expand=True)

    window.mainloop()

    dotaz = getdotaz_new.getdotazf(id_otazky, 1)
    smer = getdotaz_new.getdotazf(id_otazky, 2)

    print("id otázky:", id_otazky)
    print("dotaz: ", dotaz)
    print("smer: ", smer)
    print("----")
