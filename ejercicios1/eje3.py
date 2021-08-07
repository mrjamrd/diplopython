##Ejercicio 3
"""
 Escribir un programa que muestra los cuadrado multiplicado por si mismo 60 primeros
 naturales. Resolverlo con for y con while
"""
#while
# contador = 0
# while contador <= 60:
#     cuadrado = contador * contador
#     print(f"El cuadrado de {contador} es {cuadrado}")
#
#     contador += 1

#for

for numero in range(0,61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
