"""
Una funcion dentro de otra funcion
"""
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto


def allShow(nombre, apellido):
    texto = getNombre(nombre) +" \n  "+ getApellido(apellido)

    return texto

print(allShow("Jose Armando", "Matias Medina"))
