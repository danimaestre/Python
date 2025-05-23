import mysql.connector
from mysql.connector import Error
try:
    mi_conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = '1234'
    )



    if mi_conexion.is_connected():
        print('Conexion establecida correctamente')
        
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("SHOW DATABASES")

    for bd in mi_cursor:
        print(bd)

    mi_cursor.close()
        
    mi_conexion.close()

    if not mi_conexion.is_connected():
        print('Conexion finalizada correctamente')
except Error as e:
    print("A ocurrido un error")
    print(e)