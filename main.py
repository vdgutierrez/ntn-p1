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


@app.route('/admin/register', methods=['GET','POST'])
def register():
    print(request.form)
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        tipo = request.form['tipo']
        print(name)
        print(lastname)
        print(email)
        print(password)
        print(tipo)
        insert_perfil(name, lastname, email, password, tipo)
        if tipo == 'Asistente':
            insert_asistente(name, lastname)
        if tipo == 'Organizador':
            insert_organizador(name, lastname)
        
        if tipo == 'Orador':
            insert_orador(name, lastname)

    return render_template('admin/register.html')

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