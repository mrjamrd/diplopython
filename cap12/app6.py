from tkinter import *

ventana =Tk()

ventana.geometry("700x700")
ventana.title("Formulario en Tkinter | Jose Matias")
encabezado = Label(ventana, text="Formulario con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans",18),
    padx = 10,
    pady = 10
)
encabezado.grid(row=0,columnspan=2)

label = Label(ventana, text="nombre")
label.grid(padx=5, pady=5 ,row=1, column=0)
label = Label(ventana, text="apellido")
label.grid(padx=5, pady=5 ,row=2, column=0)
label = Label(ventana, text="mensaje")
label.grid(padx=5, pady=5 ,row=3, column=0)
campotxt1 = Entry(ventana)
campotxt1.grid(pady=5, sticky=W, row=2,column=1)
campotxt1.config(justify="left",state="normal")

#un textbox
campotxt = Entry(ventana)
campotxt.grid(pady=5, sticky=W, row=1,column=1)

campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(width=30,height=5)


btn = Button(ventana, text="Enviar")
btn.grid(row=5, column=1, sticky=W)
btn.config(padx=10, pady=10)




ventana.mainloop()
