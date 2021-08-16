"""
Una lista de contacto
"""
contactos =[
[
 'antonio',
 'Antonio@gmail.com'
],
[
 'manuel',
 'mani@gmail.com'
],
[
 'jose',
 'joseam1789@gmail.com'
]
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Es el nombre"+elemento)
        else:
            print("Es el apellido"+elemento)        
    print("\n")
