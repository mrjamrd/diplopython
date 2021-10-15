from tkinter import *

ventana =Tk()
ventana.geometry("700x700")

ventana.title("Formulario")

def getDatos():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Datos recogido: ").pack(anchor=NW)
Label(ventana, textvariable=resultado).pack(anchor=NW)

Button(ventana, text="Mostrar datos", command=getDatos).pack(anchor=NW)


ventana.mainloop()
