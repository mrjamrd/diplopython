from io import open
import pathlib

#abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
file = open(ruta,"a+")

#print(ruta)

#Escribir en el archivo

file.write("*****Soy un texto desde python escrito*****\n")

#cerrar el archivo
file.close()

file_read = open(ruta,"r")

#contenido = file_read.read()
#print(contenido)
lista = file_read.readlines()

for list in lista:
    print(list)
