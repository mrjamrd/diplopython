"""
Parametros opcionabes en funciones
opcinal
"""

def getEmpleado(nombre, dni=False):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != False:
        print(f"DNI: {dni}")


getEmpleado("Jose")
