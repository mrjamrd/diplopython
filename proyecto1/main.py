from usuarios import acciones

"""
Proyecto python y Mysqltr
- Abrir Asistente
- Login o registro
- Si elegimos Registro, Creara un usuario
- Mostrar Notas
-Crear Notas
"""


print("""
    Acciones disponibles:
        -Registro
        -Login
""")
hazEl = acciones.Acciones()
accion =  input("Que deseas hacer: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
