from tkinter import *
from tkinter import messagebox

class Calculadora:


    def __init__(self,alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        #self.alertas = alertas

    def sumar(self):
        try:
            resultado.set(float(numero1.get()) + float(numero2.get()))
            mostrarResultado()
        except:
            self.alertas.showerror("Error","Introduce los datos correcto")


    def restar(self):
        try:
            self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
            mostrarResultado()
        except:
            self.alertas.showerror("Error","Introduce los datos correcto")

    def multiplicar(self):
        try:
            self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
            mostrarResultado()
        except:
            self.alertas.showerror("Error","Introduce los datos correctos")

    def dividir(self):
        try:
            resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
            mostrarResultado()
        except ZeroDivisionError:
            self.alertas.showerror("Error", "La multiplicion por 0 no es posible")
        except:
            self.alertas.showerror("Error", "Introduce los datos correcto")

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El Resultado es:{self.resultado.get()}")
        numero1.set("")
        numero2.set("")


ventana =Tk()
ventana.title("Ejercicio completo con Tkinter | Victor Robles")

calc = Calculadora()

marco = Frame(ventana, width=250, height=200)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)



Label(marco, text="Primer numero:").pack()
Entry(marco, textvariable=calc.numero1).pack()
Label(marco, text="Segundo numero:").pack()
Entry(marco, textvariable=calc.numero2).pack()
Label(marco, text="").pack()
Button(marco, text="Sumar", command=calc.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calc.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calc.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calc.dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()
