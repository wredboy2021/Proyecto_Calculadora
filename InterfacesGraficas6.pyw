from tkinter import *
from tkinter import filedialog
Root=Tk()
def abrir():
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:",filetypes=(("Archivos Python","*.py"),("Archivos de texto","*.txt"),("Todos los archivos","*.*")))
    print(fichero)
Button(Root,text="Abrir fichero",command=abrir).pack()

Root.mainloop()