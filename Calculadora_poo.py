from tkinter import *
#Raiz
Root=Tk()
frame=Frame(Root)
frame.pack()
Root.title("Calculadora")
Numeropantalla=StringVar()
Pulsado=""
Pantalla=Entry(frame,textvariable=Numeropantalla)
Pantalla.config(justify='right',bg="black",fg="white")
Pantalla.grid(row=0,column=1,columnspan=4)


#Funciones botones

def pulsasiones(num):
       global Pulsado
       if Pulsado!="":
           Numeropantalla.set(num)
           Pulsado=""
       else:
           Numeropantalla.set(Numeropantalla.get() + str(num))
     
Uno=Button(frame,text=1,bg="Salmon",command=lambda:pulsasiones(1))
Uno.grid(row=2,column=1)
     




Root.mainloop()