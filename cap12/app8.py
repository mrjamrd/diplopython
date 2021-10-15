from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showerror("Alerta","Hola Soy Jose Armando")

def salir(nombre):
    resultado = MessageBox.askquestion("salir","Continuar ejecutando la aplicacion")
    if resultado != "si":
        MessageBox.showinfo("Adio",f"adios {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar mensaje", command=sacarAlerta).pack()

Button(ventana, text="Salir", command=lambda: salir("Jose Matias")).pack()

ventana.mainloop()
