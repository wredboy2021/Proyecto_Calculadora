from tkinter import *
Root=Tk()
frame=Frame(Root)
frame.pack()
Resultado=0
Operacion=""
Numerovariable=StringVar()
Pantalla=Entry(frame,textvariable=Numerovariable)
Pantalla.config(width=27 ,background="Black",fg="white",justify="right")
Pantalla.grid(row=1,column=1,pady=5,padx=5,columnspan=5)


#Funciones botones

def Funcionalidad(num):
    global Operacion
    Operacion=Operacion+str(num)
    if Numerovariable!="":
        Numerovariable.set(Operacion)
    else:
        Numerovariable.set(Numerovariable.get()+str(num))


def calculo(operacion): 
    global Operacion
    try:
        Operacion=str(eval(Operacion))
        Numerovariable.set(Operacion)
    except:
        Numerovariable.set("ERROR")
    Operacion = ""

def limpiarPantalla():
    global Operacion
    Operacion=""
    Pantalla.delete(0, END)




#Configuracion de botones

#Fila 1
Multiples_comandos=lambda:[Funcionalidad(1)]

One = Button(frame, text=1, bg="Salmon",command=lambda:Funcionalidad(1))
One.config(width=5)
One.grid(row=2,column=1)

Two = Button(frame, text=2, bg="Salmon", command=lambda:Funcionalidad(2))
Two.config(width=5)
Two.grid(row=2,column=2)

Tres = Button(frame, text=3, bg="Salmon", command=lambda: Funcionalidad(3))
Tres.config(width=5)
Tres.grid(row=2,column=3)

Division = Button(frame, text="/", bg="orange",command=lambda:Funcionalidad("/"))
Division.config(width=5)
Division.grid(row=2, column=4)

#Fila 2

Four = Button(frame, text=4, bg="Salmon", command=lambda: Funcionalidad(4))
Four.config(width=5)
Four.grid(row=3, column=1)

Five = Button(frame, text=5, bg="Salmon", command=lambda: Funcionalidad(5))
Five.config(width=5)
Five.grid(row=3, column=2)

Six = Button(frame, text=6, bg="Salmon", command=lambda: Funcionalidad(6))
Six.config(width=5)
Six.grid(row=3, column=3)

Multiplicacion = Button(frame, text="*", bg="orange",command=lambda:Funcionalidad("*"))
Multiplicacion.config(width=5)
Multiplicacion.grid(row=3, column=4)

#Fila 3

Seven = Button(frame, text=7, bg="Salmon", command=lambda: Funcionalidad(7))
Seven.config(width=5)
Seven.grid(row=4, column=1)

ocho = Button(frame, text=8, bg="Salmon", command=lambda: Funcionalidad(8))
ocho.config(width=5)
ocho.grid(row=4, column=2)

nueve = Button(frame, text=9, bg="Salmon", command=lambda: Funcionalidad(9))
nueve.config(width=5)
nueve.grid(row=4, column=3)

Resta = Button(frame, text="-", bg="orange",command=lambda:Funcionalidad("-"))
Resta.config(width=5)
Resta.grid(row=4, column=4)

#Fila 4

Suma = Button(frame, text="+", bg="orange",command=lambda:Funcionalidad("+"))
Suma.config(width=5)
Suma.grid(row=5, column=1)

cero = Button(frame, text=0, bg="Salmon", command=lambda: Funcionalidad(0))
cero.config(width=5)
cero.grid(row=5, column=2)

coma = Button(frame, text=",", bg="orange", command=lambda: Funcionalidad(","))
coma.config(width=5)
coma.grid(row=5, column=3)

igual = Button(frame, text="=", bg="orange",command=lambda:calculo(Operacion))
igual.config(width=5)
igual.grid(row=5, column=4)

#fila de opciones extra

borrar = Button(frame, text="DEL", bg="orange",command=lambda:limpiarPantalla())
borrar.config(width=5)
borrar.grid(row=6, column=2)

Modulo = Button(frame, text="%", bg="orange",command=lambda:Funcionalidad("%") )
Modulo.config(width=5)
Modulo.grid(row=6, column=3)

Potenciacion= Button(frame, text="**",bg="orange",command=lambda:Funcionalidad("**"))
Potenciacion.config(width=5)
Potenciacion.grid(row=6,column=4)




Root.mainloop()




