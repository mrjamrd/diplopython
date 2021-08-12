"""
Funciones con parametros
def nombreFunciones(parametro):
    #codigo
    #codigo
"""

nombre = input("Digite un nombre: ")
edad = int(input("Gigite una Edad: "))
def mostrarNombre(nombre,edad):
    print(f"Nombre es: {nombre}")
    if edad >= 18:
        print("Eres mayor de edad")


mostrarNombre(nombre,edad)
