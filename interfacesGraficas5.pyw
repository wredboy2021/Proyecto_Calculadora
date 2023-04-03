from tkinter import *
from tkinter import messagebox
Root=Tk()

def Ventana_Informacion():
    messagebox.showinfo("SebastianGod","Procesos realizados")
def licencia():
    messagebox.showwarning("Licencia","Producto Licenciado por el dios sebastian")
def salir():
   Val=messagebox.askquestion("Salir","Desea salir de la aplicacion?")
   if Val=="yes":
       Root.quit()
def cerrardocumento():
    Val=messagebox.askretrycancel("Reintentar","No es posible cerrar el documento")


Barramenu=Menu(Root)
Root.config(menu=Barramenu,width=300,height=300)
ArchivoMenu=Menu(Barramenu,tearoff=0)
ArchivoAyuda=Menu(Barramenu,tearoff=0)
ArchivoEdicion=Menu(Barramenu,tearoff=0)
ArchivoHerramientas=Menu(Barramenu,tearoff=0)
#Archivo barra menu
ArchivoMenu.add_command(label="Guardar todo")
ArchivoMenu.add_command(label="Abrir Un Archivo")
ArchivoMenu.add_command(label="Nuevo Archivo")
ArchivoMenu.add_command(label="Guardar")
ArchivoMenu.add_command(label="Salir",command=salir)
# Archivo Herramientas
ArchivoHerramientas.add_command(label="Copiar")
ArchivoHerramientas.add_command(label="Pegar")
ArchivoHerramientas.add_separator()
ArchivoHerramientas.add_command(label="Eliminar Archivo")
ArchivoHerramientas.add_command(label="Buscar")
#Archivoayuda
ArchivoAyuda.add_command(label="Acerca de...",command=Ventana_Informacion)
ArchivoAyuda.add_command(label="Licencia",command=licencia)

Barramenu.add_cascade(label="Archivo",menu=ArchivoMenu)
Barramenu.add_cascade(label="Ayuda",menu=ArchivoAyuda)
Barramenu.add_cascade(label="Edicion",menu=ArchivoEdicion)
Barramenu.add_cascade(label="Herramientas",menu=ArchivoHerramientas)






Root.mainloop()