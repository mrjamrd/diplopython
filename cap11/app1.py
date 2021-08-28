"""

"""
import mysql.connector

#conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)
#print(database)
cursor = database.cursor(buffered=True)

#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# cursor.execute("SHOW DATABASES")
#
# for db in cursor:
#     print(db)

#Crear Tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT PK_vehiculo PRIMARY KEY(id)
)
""")
##Mostrar tablas en python
#cursor.execute("SHOW TABLES")

# for db in cursor:
#     print(db)

##Insertar datos en mysql
##cursor.execute("INSERT INTO vehiculos VALUES(null, 'Toyoya', 'Corrolla',10000)")
# autos = [
#  ('seat','ibiza',50000),
#  ('Renault','CLio',15500),
#  ('Citroen','Saxo',20000),
#  ('Mercedes','Clase c', 35000)
# ]
# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s,%s,%s)",autos)
# database.commit()

#Leer datos desde python en mysql

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for item in result:
    print(item)

###Borrar Datos  en mysql
# cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
# database.commit()

###Actualizar datos en mysql
# cursor.execute("UPDATE vehiculos SET modelo='camry' WHERE marca='Toyota' ")
# database.commit()

###Actualizar la marca  de la base de datos
# cursor.execute("UPDATE vehiculos SET marca='toyota' WHERE marca='toyoya'")
# database.commit()
