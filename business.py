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

