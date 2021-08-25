"""
Conexion de base de datos 

importar el sqlite3

conexion = sqlite3.connect("prueba.db")
cursos = conexion.cursor()
cursor.execute()
conexion.close()

"""
import sqlite3

conexion = sqlite3.connect('prueba.db')

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo varchar(255), "+
"descricion text, "+
"precio int(255)"+
" )")
conexion.commit()


## Insertar datos 

cursor.execute("INSERT INTO productos VALUES (null, 'primir producto', 'Descripcion de producto',505)")
conexion.commit()


##selecionar 
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
for item in productos:
    print(item)
conexion.close()
