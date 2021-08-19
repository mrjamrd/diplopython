"""
Ejercicio 4: Crear un scriopt que tenga 4 variable, un lista, un string
"""

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    if test:
        result = f"Este datos es del tipo {type(dato)}"
    else:
        result = "El tipo de dato no es correcto"
    return result

mi_lista = ["Jose Matias",77]
titulo = "Master en python"
verdadero = True


print(comprobarTipado(mi_lista, list))
