from flask import Flask, render_template, request, flash, session, redirect, url_for
from business import *

app = Flask(__name__)
app.secret_key = 'Arqui123'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Usar la función db_connection() para conectar a la base de datos
        conexion = db_connection()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            # Verificar si el usuario existe en la base de datos
            cursor.execute('SELECT * FROM PERFIL WHERE CORREO = %s AND CONTRASENA = %s', (email, password))
            user = cursor.fetchone()
            conexion.close()  # Cierra la conexión después de la consulta
            
            if user:
            
                return redirect(url_for('conferencias'))  # Usa el nombre de la función de ruta
            else:
                flash('Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.', 'error')
                return redirect(url_for('login'))
        else:
            flash('Error al conectar a la base de datos.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/admin/registro_conferencia')
def conferencia():
    return render_template('admin/registro_conferencia.html')

@app.route('/admin/navbar_admin')
def navbar_admin():
    return render_template('admi/navbar_admin.html')

@app.route('/asistente/conferencias')
def conferencias():
    return render_template('asistente/conferencias.html')

@app.route('/asistente/votacion')
def votacion():
    return render_template('asistente/votacion.html')

@app.route('/asistente/evaluacion')
def evaluacion():
    return render_template('asistente/evaluacion.html')

@app.route('/asistente/navbar_asistente')
def navbar_asistente():
    return render_template('admi/navbar_asistente.html')


# @app.route('/admin/register', methods=['GET','POST'])
# def register():
#     print(request.form)
#     if request.method == 'POST':
#         name = request.form['name']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         password = request.form['password']
#         tipo = request.form['tipo']
#         print(name)
#         print(lastname)
#         print(email)
#         print(password)
#         print(tipo)
#         insert_perfil(name, lastname, email, password, tipo)
#         if tipo == 'Asistente':
#             insert_asistente(name, lastname)
#         if tipo == 'Organizador':
#             insert_organizador(name, lastname)
        
#         if tipo == 'Orador':
#             insert_orador(name, lastname)

#     return render_template('admin/register.html')

def insert_perfil(name, lastname, email, password, tipo):
    conexion = db_connection()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        usuario = f"{name} {lastname}"
        cursor.execute(
            "INSERT INTO PERFIL (USUARIO, CONTRASENA, CORREO, TIPO) VALUES (%s, %s, %s, %s)",
            (usuario, password, email, tipo)
        )
        conexion.commit()

        id_perfil = cursor.lastrowid
        if tipo == 'asistente':
            insert_asistente(name, lastname, id_perfil)
        elif tipo == 'organizador':
            insert_organizador(name, lastname, id_perfil)
        elif tipo == 'orador':
            insert_orador(name, lastname, id_perfil)
        else:
            return "Tipo de usuario no válido", 400

    except Error as e:
        print(f"Error al insertar en PERFIL: {e}")
    finally:
        cursor.close()
        conexion.close()

def insert_asistente(name, lastname, id_perfil):
    conexion = db_connection()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO ASISTENTE (NOMBRES, APELLIDOS,ID_PERFIL) VALUES (%s, %s, %s)",
            (name, lastname, id_perfil)
        )
        conexion.commit()
    except Error as e:
        print(f"Error al insertar en ASISTENTE: {e}")
    finally:
        cursor.close()
        conexion.close()

def insert_organizador(name, lastname, id_perfil):
    conexion = db_connection()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO ORGANIZADOR (NOMBRES, APELLIDOS, ID_PERFIL) VALUES (%s, %s, %s)",
            (name, lastname, id_perfil)
        )
        conexion.commit()
    except Error as e:
        print(f"Error al insertar en ORGANIZADOR: {e}")
    finally:
        cursor.close()
        conexion.close()

def insert_orador(name, lastname, id_perfil):
    conexion = db_connection()
    if conexion is None:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO ORADOR (NOMBRES, APELLIDOS, ID_PERFIL) VALUES (%s, %s, %s)",
            (name, lastname, id_perfil)
        )
        conexion.commit()
    except Error as e:
        print(f"Error al insertar en ORADOR: {e}")
    finally:
        cursor.close()
        conexion.close()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        tipo = request.form.get('tipo')
        
        print(f"Nombre: {name}")
        print(f"Apellido: {lastname}")
        print(f"Correo: {email}")
        print(f"Contraseña: {password}")
        print(f"Tipo: {tipo}")

        # Verifica que todos los campos se han llenado
        if not all([name, lastname, email, password, tipo]):
            return "Todos los campos son obligatorios", 400

        # Inserta datos en la base de datos
        insert_perfil(name, lastname, email, password, tipo)

        return redirect(url_for('conferencias'))

    return render_template('register.html')



@app.route('/metting')
def metting():
    return render_template('metting.html')

@app.route('/login_user', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
    return 'received'






if __name__ == '__main__':
    app.run(debug=True)