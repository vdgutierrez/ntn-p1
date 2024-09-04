import mysql.connector as mysql

def db_connection():
    conexion = mysql.connect(
        host="sql10.freemysqlhosting.net",
        user="sql10729427",
        password="ji7RdGLaZq",
        database="sql10729427",
        port=3306
    )
    print(conexion)
    return conexion