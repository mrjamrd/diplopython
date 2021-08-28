import sqlite3

conexion = sqlite3.connect("estu.db")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre varchar(255),
apellido varchar(255),
edad int(255)
)
""")

conexion.commit()

#insertar datos

# cursor.execute("INSERT INTO estudiantes VALUES (null, 'segundo estudiante', 'Apellido del estudiante',12)")
# conexion.commit()

##Listar los estuiantes

cursor.execute("SELECT * FROM estudiantes")

estudiantes = cursor.fetchall()

for estudiante in estudiantes:
    print(estudiante)

estudiantes = cursor.fetchone()

print(estudiantes)
conexion.commit()

##Actualizar Registro
cursor.execute("UPDATE estudiantes SET edad=14 WHERE edad=13")
conexion.commit()


##Borrar todo
# cursor.execute("DELETE FROM estudiantes")
# conexion.commit()

###Insertar varios registro a la vez

# estudi = [
# ("estudiante1","apellido est",12 ),
# ("estudiante1","apellido est",13 ),
# ("estudiante1","apellido est",11 ),
# ("estudiante1","apellido est",13 ),
# ("estudiante1","apellido est",14 ),
# ]
#
# cursor.executemany("INSERT INTO estudiantes VALUES (null,?,?,?)", estudi)
# conexion.commit()

conexion.close()
