from tkinter import *

ventana =Tk()
ventana.geometry("500x500")
saludo = "hola desde la variable"

texto1 = Label(ventana, text=saludo)
texto1.config(
    fg="white",
    bg="#000000",
    padx=120,
    pady=20,
    font=("Arial", 30),
    cursor="spider"
)
texto1.pack()
texto = Label(ventana, text='Jose Armando Matias')
texto.config(
    fg="red"

)
texto.pack(anchor=SW)
hola = Button(ventana,text='Hola')
hola.config(
    fg="blue",
    cursor="spider"
)
hola.pack()

ventana.mainloop()
