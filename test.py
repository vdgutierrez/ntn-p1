import mysql.connector as mysql
from mysql.connector import Error

def db_connection():
    try:
        conexion = mysql.connect(
            host="localhost",
            user="root2",
            password="12345678",
            database="Arqui1",
            port=3308
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

    return conexion

# Ejemplo de uso:
conexion = db_connection()
if conexion:
    # Tu código para interactuar con la base de datos aquí
    conexion.close()  # Cierra la conexión cuando termines
