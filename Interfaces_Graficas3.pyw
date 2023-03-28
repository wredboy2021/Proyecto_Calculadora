from tkinter import *
Root=Tk()
Varopcion=IntVar()
def imprimir():
    #print(Varopcion.get())
    if Varopcion.get()==1:
        Etiqueta.config(text="Eres un hombre")
    else:
        Etiqueta.config(text="Eres una mujer")

Label(Root,text="Genero:").pack()
Masculino=Radiobutton(Root,text="Masculino",variable=Varopcion,value=1,command=imprimir).pack()
Femenino=Radiobutton(Root,text="Femenino",variable=Varopcion,value=2,command=imprimir).pack()
Etiqueta=Label(Root)
Etiqueta.pack()


Root.mainloop()