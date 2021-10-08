from tkinter import *

ventana = Tk()

ventana.title("Bienvenido")
ventana.geometry("500x400")

texto = Label(ventana,text='hola como esta')
texto.pack()

ventana.mainloop()
