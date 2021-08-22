from io import open
import pathlib
import shutil


#mover o renonbrar archivo

ruta = str(pathlib.Path().absolute()) + "/fichero_textonew.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

shutil.move(ruta, ruta_nueva)
