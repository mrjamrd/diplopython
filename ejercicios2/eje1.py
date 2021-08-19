"""
Ejercicio Iniciamos segundo bloque
hacer un programa de 8 numeros enteros y haga lo siguiente
Recorrer la lista y mostrarla
ordenarla y mostrarla
mostrar sus longitud
buscar algun elemento
"""

numeros = [13,64,52,73,21,7,91,63]
def mostrarLista(lista):
    resultado =""
    for elemento in lista:
        resultado  += "elemento: " +str(elemento)
        resultado += "\n"
    return resultado

# Recorrer y Mostrar
# for numero in numeros:
#     print(numero)

print(mostrarLista(numeros))
numeros.sort()
print(mostrarLista(numeros))

print(len(numeros))

busqueda = int(input("Introduce el numero: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <=0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introduciodo el {busqueda}")
print(f"Busqueda en la lista el numero {busqueda}")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indece: {search}")
