#Ejercicio 7
"""
Crear un programa que muestre todos los numeros inpares

"""

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce el siguiente numero: "))

if numero1 < numero2:
    for x in range(numero1 , (numero2+1)):
        if x % 2 ==0:
            print(f"numero es par {x}")
        else:
            print(f"Numero es impar {x}")
                
else:
    print("El numero 1 debe ser mayor al numero 2")
