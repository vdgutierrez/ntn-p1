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

@app.route('/admin/registro_conferencia', methods=['GET', 'POST'])
def conferencia():
    if request.method == 'POST':
        # Obtener datos del formulario
        title = request.form.get('title')
        location = request.form.get('location')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        link = request.form.get('link')
        description = request.form.get('description')
        
        # Verificar que todos los campos se han llenado
        if not all([title, location, start_date, end_date, link, description]):
            return "Todos los campos son obligatorios", 400
        print(str(title)+" "+str(location)+" "+str(start_date)+" "+str(end_date)+" "+str(link)+" "+str(description))
        # Insertar datos en la base de datos
        insert_conference(title, location, start_date, end_date, description, link)
        
        # Redirigir a la misma página para mostrar el formulario y la lista actualizada de conferencias
        return redirect('/asistente/conferencias')
    
    # Conectar a la base de datos
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Consultar las conferencias
    cursor.execute("SELECT nombre, detalle, f_inicio, f_fin, ubicacion, marca FROM conferencia ORDER BY id_conferencia DESC")
    conferences = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    connection.close()
    
    # Pasar los datos a la plantilla
    return render_template('/admin/registro_conferencia.html', conferences=conferences)

def insert_conference(nombre, ubicacion, f_inicio, f_fin, detalle, marca):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO conferencia (nombre, detalle, f_inicio, f_fin, ubicacion, marca, ID_organizador)
        VALUES (%s, %s, %s, %s, %s, %s, 1)
    """, (nombre, detalle, f_inicio, f_fin, ubicacion, marca))
    connection.commit()
    cursor.close()
    connection.close()


@app.route('/admin/navbar_admin')
def navbar_admin():
    return render_template('admi/navbar_admin.html')

@app.route('/asistente/conferencias')
def conferencias():
    # Conectar a la base de datos
    connection = db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Consultar las conferencias
    cursor.execute("SELECT nombre, detalle, f_inicio, f_fin, ubicacion, marca FROM conferencia ORDER BY id_conferencia DESC")
    conferences = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    connection.close()
    
    # Pasar los datos a la plantilla
    return render_template('asistente/conferencias.html', conferences=conferences)


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