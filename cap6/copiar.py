from io import open
import pathlib
import shutil

#copiar archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
rutanueva = str(pathlib.Path().absolute()) + "/fichero_texto1.txt"
shutil.copyfile(ruta,rutanueva)
