"""
#bucle while
estructura de control que itera o repite la ejecucion de una serie de instruciones
tantas veces

while condicion:
    bloque de instruciones
    actualizacion
"""
contador = 1

while contador <=100:
    print(f"Estoy en ele numero: {contador}")
    contador=contador + 1
###/////////////////////////////////////////////////////////////////////////////////

numero_user = int(input("De que numero Quiere la Tabla: "))
contador = 1
if numero_user <1:
    numero_user = 1
while contador <= 10:
    print(f"{numero_user} X {contador} = {numero_user * contador}")

    contador =+ 1
