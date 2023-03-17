from tkinter import *
#Configurando la raiz del programa
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame1.pack()
frame2.pack()
Nombre=StringVar()

texto = Entry(frame1,textvariable=Nombre)
texto.grid(row=0, column=2, pady=5,padx=5)

texto1 = Entry(frame1)
texto1.grid(row=1, column=2, pady=5)

texto2 = Entry(frame1)
texto2.grid(row=2, column=2, pady=5)

texto3=Entry(frame1)
texto3.grid(row=3,column=2,pady=5)
texto3.config(show="*")

texto4=Text(frame1,width=20,height=5)
texto4.grid(row=4,column=2,pady=5)

VarScroll=Scrollbar(frame1,command=texto4.yview)
VarScroll.grid(row=4,column=3,sticky="nsew")
texto4.config(yscrollcommand=VarScroll.set)
#Pasando a la parte de edicion de Cuadros de texto

cuadro_de_texto = Label(frame1, text="Nombre:",cursor="pirate", font=("Calibri", 10), fg="blue")
cuadro_de_texto.grid(row=0, column=0,pady=5)
cuadro_de_texto.config(justify="center")

cuadro_de_texto1 = Label(frame1, text="Apellido", cursor="pirate", fg="orange")
cuadro_de_texto1.grid(row=1, column=0, pady=5)

cuadro_de_texto2 = Label(frame1, text="Edad:", cursor="pirate", fg="red")
cuadro_de_texto2.grid(row=2, column=0, pady=5)

cuadro_de_texto3 = Label(frame1, text="Contraseña:", cursor="pirate", fg="green")
cuadro_de_texto3.grid(row=3, column=0, pady=5)

cuadro_de_texto4 = Label(frame1, text="Biografia:", cursor="pirate", fg="purple")
cuadro_de_texto4.grid(row=4, column=0, pady=5)


 
def Autoboton():
    Nombre.set("Sebastian")
    

Enviar=Button(frame2,text="Envia",command=Autoboton)
Enviar.pack()



root.mainloop()
