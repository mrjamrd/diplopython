from io import open
import pathlib
import shutil
import os
import os.path
#eliminar
#ruta = str(pathlib.Path().absolute()) + "/fichero_textonew.txt"
#os.remove(ruta)

#print(os.path.absolute("./"))
#ruta = os.path.abspath("./") + "/fichero_texto1.txt"

ruta = "./fichero_texto1.txt"

#Comprobar si existe un archivo en una ruta

if os.path.isfile(ruta):
    print("El archivo existe")
else:
    print("El Archivo no existe")
