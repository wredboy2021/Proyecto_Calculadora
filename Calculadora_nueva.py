from tkinter import *
#Raiz
Root=Tk()
frame=Frame(Root)
frame.pack()
Numeropantalla=StringVar()
Pulsado=""
Pantalla=Text(frame,textvariable=Numeropantalla)
Pantalla.config(width=120,bg="black",fg="white",justify="right")
Pantalla.grid(row=1,column=10)

#Funciones botones
class funciones():
    def __init__(self,suma,resta,multiplicacion,division):
        self.suma=suma
        self.resta=resta
        self.multiplicacion=multiplicacion
        self.divison=division
    def pulsasiones(num):
       global Pulsado
       if Pulsado!="":
           Numeropantalla.set(num)
           Pulsado=""
       else:
           Numeropantalla.set(Numeropantalla.get + str(num))


#Botones








Root.mainloop()