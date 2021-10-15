from tkinter import *
from tkinter import messagebox

ventana =Tk()
ventana.title("Ejercicio completo con Tkinter | Victor Robles")
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=200)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error","Introduce los datos correcto")


def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error","Introduce los datos correcto")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error","Introduce los datos correctos")

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except ZeroDivisionError:
        messagebox.showerror("Error", "La multiplicion por 0 no es posible")
    except:
        messagebox.showerror("Error", "Introduce los datos correcto")

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El Resultado es:{resultado.get()}")
    numero1.set("")
    numero2.set("")


Label(marco, text="Primer numero:").pack()
Entry(marco, textvariable=numero1).pack()
Label(marco, text="Segundo numero:").pack()
Entry(marco, textvariable=numero2).pack()
Label(marco, text="").pack()
Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()
