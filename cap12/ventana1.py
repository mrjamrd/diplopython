from tkinter import *
import os.path
ventana = Tk()

#para el tamaño de la ventana
ventana.geometry("500x500")
ventana.title("Bienvenido")
##comprovar
ruta_icono = os.path.abspath("./img/logo.ico")

#mostrar texto
texto = Label(ventana, text=ruta_icono)
texto.pack()

#para saber si una ruta funciona 
if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath("./cap12/img/logo.ico")


ventana.iconbitmap(ruta_icono)
ventana.resizable(0,0)
#Arrancar y mostrar la ventana hasta qye se cierre
ventana.mainloop()
