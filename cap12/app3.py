from tkinter import *
from PIL import Image, ImageTk
ventana = Tk()

ventana.geometry("800x800")
Label(ventana, text='jose Armando Matias').pack(anchor=W)

img = Image.open('./img/lobo1.jpg')
render = ImageTk.PhotoImage(img)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()
