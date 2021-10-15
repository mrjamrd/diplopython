from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Marcos - De python")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
    bd=12,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)
marco.pack_propagate(False)
Label(marco, text='hola en el marco').pack()

ventana.mainloop()
