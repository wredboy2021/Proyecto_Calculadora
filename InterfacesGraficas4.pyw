from tkinter import *
Root=Tk()
Playa=IntVar()
Mountain=IntVar()
Turismo=IntVar()
Foto=PhotoImage(file="c.png")
llabel=Label(Root,image=Foto).pack()
Frame1=Frame(Root)
Frame1.pack()
Mostrar=Label(Frame1)
Mostrar.pack()
def imprimir():
    Opcion=""
    if Playa.get()==1:
        Opcion+="Has elegido la playa\nQue disfrutes tus vacaciones"
    elif Mountain.get()==1:
        Opcion+="Has elegido la Mountain\nQue disfrutes tus vacaciones"
    elif Turismo.get():
        Opcion="Has elegido El turismo por la ciudad\nQue disfrutes tus vacaciones"
    Mostrar.config(text=Opcion)

Label(Frame1,text="Elija opciones de viaje",width=50).pack()
turismo=Checkbutton(Frame1,text="Turismo",command=imprimir,variable=Turismo,onvalue=1,offvalue=0).pack()
montaña=Checkbutton(Frame1,text="Montaña",command=imprimir,variable=Mountain,onvalue=1,offvalue=0).pack()
playa=Checkbutton(Frame1,text="Playa",command=imprimir,variable=Playa,onvalue=1,offvalue=0).pack()

Root.mainloop()