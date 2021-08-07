#Ejercicio 4
"""
Pedir 2 numeros al usuario y hacer todas las operaciones basicas de una calculadora
motrarlo por pantallas.

"""
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
divicion = numero1 / numero2

print(f"El resultado de la suma {numero1} + {numero2} es: {suma}")
print(f"El resutaldo de la multiplicacion {numero1} * {numero2} es: {multiplicacion}")
print(f"El resultado de la Resta {numero1} - {numero2} es: {resta}")
print(f"El resultado de la divicion {numero1} / {numero2} es: {divicion}")
