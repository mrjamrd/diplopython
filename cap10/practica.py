import sqlite3


conexion = sqlite3.connect("persona")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS personas(
id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
nombre varchar(255),
apellido varchar(255),
edad varchar(255)
) 
""")

conexion.commit()

cursor.execute("INSERT INTO personas VALUES(null,'Jose','Baez','26')")

conexion.commit()

cursor.execute("SELECT * FROM personas where apellido='matias' ")
personas = cursor.fetchall()
for persona in personas:
    print(persona)

conexion.close()
