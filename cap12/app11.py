from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

encabezado = Label(ventana, text="Formulario 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)


#botoes check
Label(ventana, text="Aque te dedicas?").pack()
Checkbutton(ventana, text="Desarrollo web").pack()
Checkbutton(ventana, text="Desarrollo web").pack()

#RadioButtoncc
Radiobutton(ventana, text="Masculino").pack()
Radiobutton(ventana, text="Femenino").pack()

#option menu
select = OptionMenu(ventana, "Opcion 1", "Opcion 1", "Opcion 2","Opcion 3")
select.pack()
ventana.mainloop()
