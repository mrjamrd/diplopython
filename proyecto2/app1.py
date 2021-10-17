from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto en Tkinter")
ventana.resizable(0,0)
#Defirnir
home_label = Label(ventana, text="inicio")
info_label = Label(ventana, text="Informacion del programador")
add_label = Label(ventana, text="Añadir Producto")
#pantallas
def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    home_label.grid_remove()
    add_label.grid_remove()

#cargar informacion
info()



def add():

    add_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    home_label.grid_remove()
    info_label.grid_remove()

#cargar agregar
add()

def home():

    home_label.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
    add_label.grid_remove()
    info_label.grid_remove()
#cargar pantalla home
home()



#crear menu
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=menu_superior)

#cargar ventana
ventana.mainloop()
