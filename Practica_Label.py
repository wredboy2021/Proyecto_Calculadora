
from tkinter import *
Raiz = Tk()
Raiz.iconbitmap("perros-pug.ico")
Raiz.config(bg=("white"))
Frame_lame = Frame(Raiz, height=1000, width=1000)
Frame_lame.pack()
Label(Frame_lame,text="Hola mundo pero en interfaz grafica",cursor="pirate",fg="Blue",bg="Red",font=("Calibri",18)).place(x=100, y=200)
Raiz.mainloop()
print("")
#Hola como estan esto es una prueba