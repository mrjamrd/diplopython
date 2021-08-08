#Ejercicio 8

"""
Cuanto es el x porciento de x de un numero
"""
numero1 = int(input("Digite un numero: "))
numeroporciento = int(input("Digite el porciento quieres: "))

operacion = (numero1 * (numeroporciento/100))

print(f"El {numeroporciento}% de {numero1} es {operacion}")
