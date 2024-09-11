import mysql.connector as mysql
from mysql.connector import Error

def db_connection():
    try:
        conexion = mysql.connect(
            host="localhost",
            user="root1",
            password="12345678",
            database="Arqui2",
            port=3308
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

    return conexion

def read_data():
    connetion = db_connection()
    cursor = connetion.cursor()
    cursor.execute("SELECT * FROM PERSONAL")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connetion.close()

def insert_perfil(name, lastname, email, password, tipo):
    connetion = db_connection()
    cursor = connetion.cursor()
    usuario = name + ' ' + lastname
    cursor.execute("INSERT INTO PERFIL (USUARIO,CONTRASENA, CORREO, TIPO) VALUES (%s, %s, %s, %s)", (usuario, password, email, tipo))
    connetion.commit()
    cursor.close()
    connetion.close()

def insert_asistente(name, lastname):
    connetion = db_connection()
    cursor = connetion.cursor()
    cursor.execute("INSERT INTO ASISTENTE (NOMBRES, APELLIDOS) VALUES (%s, %s)", (name, lastname))
    connetion.commit()
    cursor.close()
    connetion.close()

def insert_organizador(name, lastname):
    connetion = db_connection()
    cursor = connetion.cursor()
    cursor.execute("INSERT INTO ORGANIZADOR (NOMBRES, APELLIDOS) VALUES (%s, %s)", (name, lastname))
    connetion.commit()
    cursor.close()
    connetion.close()

def insert_orador(name, lastname):
    connetion = db_connection()
    cursor = connetion.cursor()
    cursor.execute("INSERT INTO ORADOR (NOMBRES, APELLIDOS) VALUES (%s, %s)", (name, lastname))
    connetion.commit()
    cursor.close()
    connetion.close()

