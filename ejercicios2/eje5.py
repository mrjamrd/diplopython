"""
Ejercicio 5:
"""
tabla = [

    {
      "categoria" : "accion",
      "juegos" : ["gta","Call of duty", "PUGB"]

    },
    {
        "categoria" : "Aventura",
        "juegos" : ["ASSASINS", "Crash bandigo", "Prince of persia"]
    },
    {
        "categoria" : "Deporte",
        "juegos" : ["fifa 21","pes","Moto GP 21"]
    }
]

for categoria in tabla:
    print(f"---------{categoria['categoria']}----------")
    for juego in categoria['juegos']:
        print(juego)
