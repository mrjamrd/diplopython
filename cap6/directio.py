import os, shutil

#crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")


#Eliminar carpeta
#os.rmdir('./mi_carpeta_new')


###Copiar directorio
"""
ruta = "./mi_carpeta"
ruta_new = "./mi_carpeta_new"

shutil.copytree(ruta, ruta_new)
"""
##Lista contenido de un directorio :

print("Listar contenido")
contenido = os.listdir("./mi_carpeta")
for item in contenido:
    print(f"fichechos: {item}")
