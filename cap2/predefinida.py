"""
Funcion predefinida por el lenguaje de programacion
"""
nombre = "Jose Armando"
print(type(nombre))

comprobar  = isinstance(nombre, str)

if comprobar:
    print("Esa variable es un string")
else:
    print("Es una cadena")

if not isinstance(nombre, float):
    print("La variable")

frase = "mi contenido"

print(frase)
print(frase.strip())
year = 2021
print(year)
del year

texto =" ff "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La varibale tiene contenido", len(texto))

frase = "la vida es bella"

print(frase.find("vida"))


nueva = "La vida es bella"
nueva_f = nueva.replace("vida","moto")
print(nueva_f)
