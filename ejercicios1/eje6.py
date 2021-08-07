#Ejercicio 6
"""
Crear todas la tabla de multiplicar del 1 al 10
 Montrando el titulo de las tablas
"""

for cabecera in range(1,11):

    print("#######################################")
    print(f"#La tabla es {cabecera}#")
    print("#######################################")

    for numero in range(1,11):
        print(f"{cabecera} X {numero}  = {numero * cabecera}")

    print("\n")
