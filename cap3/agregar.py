"""
Agregar mas nombre desde el nombre
"""
nombre = ["jose","Armando"]

nombre_add = ""

while nombre_add != "parar":
    nombre_add = input("Agregar Nombre: ")
    nombre.append(nombre_add)

for n in nombre:
    print("el nombre es: "+ str (n))
