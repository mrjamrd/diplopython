"""
Ejercicio 3: Hacer un programa que compruebe una variable este vacia

"""
texto = ""

if len(texto.strip()) <=0:
    texto = "Hola soy un texto"
    print(texto.upper())

else:
    print(f"La variable tiene contenido {texto}")
