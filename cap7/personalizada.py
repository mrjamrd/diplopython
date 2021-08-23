"""
 => Personalizando los errores usando ValueError con raise
 => Luego atrapando el valor con except
 => Asi para tener mas claro los manejos de errores
 => 
"""
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad no es Real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no esta completo")

    else:
        print(f"bienvenido al master de python: {nombre}")

except ValueError:
    print("Introduce los datos correctos")
