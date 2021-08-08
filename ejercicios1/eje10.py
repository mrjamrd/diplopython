#Ejercicio 10
"""
 El programa tiene que pedir la nota de 15 alumnos y sacar por pantallas
 cuantos han aporbado y cuantos han suspendido
"""
contador = 1
aprobados = 0
suspendidos = 0
numero_alumnos = int(input("Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input("Que no quiere ponerles al estudiante: "))

    if nota >=5:
        aprobados +=1
    else:
        suspendidos += 1
    contador += 1

print(f"\n Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendido: {suspendidos}")
