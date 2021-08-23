##multiples excepciones
try:

    numero = int(input("Numero para elevarlo: "))
    print("El cuadrado de un numero: "+ str(numero*numero))

# except ValueError:
#     print("De introducir un numero")
#
# except TypeError:
#     print("Debe convertir tu cadena en entero")

except Exception as e:
    print("Ha ocurrido un error ", type(e).__name__)
