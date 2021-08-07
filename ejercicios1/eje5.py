#Ejecicio 5
"""
Hacer un programa muestro todos los numero entre 2 numeros que diga el usuario.
"""

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero:"))

if numero1 < numero2:

    for contador in range(numero1, (numero2+1)):
        print(f"{contador}")
else:
    print(f"El numero 1 debe ser menor al numero 2")
