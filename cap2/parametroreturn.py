"""
Parametros opcionales y return o devuelve datos
"""
def saludame(nombre):
    saludo = f"Hola, saludo {nombre}"

    return saludo


print(saludame("Jose Armando"))


def calculadora(num1, num2, basicas = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divicion = num1 / num2

    cadena = ""
    if basicas != False:
        cadena +="Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multipicacion: " + str(multi)
        cadena += "\n"
        cadena += "Divicion: " + str(divicion)

    return cadena

print(calculadora(10,5,True))
