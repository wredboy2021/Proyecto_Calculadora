from tkinter import *
class Calculadora():
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora Poo")
        self.frame1=Frame(ventana_Principal)
        self.frame1.grid(row=1,column=1)
        self.Numeropantalla=StringVar()
        self.Operaciones=""
        self.Pantalla=Entry(self.frame1,textvariable=self.Numeropantalla)
        self.Pantalla.grid(row=0,column=1,columnspan=4,padx=10,pady=10)
        self.Pantalla.config(width=27,bg="Black",fg="white")
        Uno=Button(text=1,fg="red",bg="Black",foreground="white")
        Uno.grid(row=2,column=0)
        return
    




    
    def Creacion_Botones():
        pass




ventana_Principal=Tk()
Calculadora=Calculadora(ventana_Principal)
ventana_Principal.mainloop()
