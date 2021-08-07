# Ejercicio 2
"""
Escribir un script que nos muestren por pantalla todos
los numeros pares de 1 al 120
% -> Para buscar el residuo en el la divicion 
"""
contador = 1

for contador in range(1,121):
    if contador % 2 == 0:
        print(str(contador))
