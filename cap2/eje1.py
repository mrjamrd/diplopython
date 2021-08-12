"""
Tabla de multiplicar
"""


def tabla(numero):
    print(f"Tabla de multiplicar {numero}")

    for contador in range(1,11):

        op = numero * contador
        print(f"{numero} X {contador} = {op}")

for tabla_multi in range(1,11):
    tabla(tabla_multi)
