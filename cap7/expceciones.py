"""
excepciones para Manejo de  errores

Captuirar excepciones y manejar errores en codigo

"""
try:
    nombre  = input("Cual es tu nombre: ")

    if len(nombre) >1:
        nombre_usuario = "EL nombre es " + nombre
    print(nombre_usuario)

except:
    print("Ha ocurrido un error Introduce bien el nombre")

else:
    print("Todo ha funcionado correctamente")

finally:
    print("fin de la iteracion!!!!")
