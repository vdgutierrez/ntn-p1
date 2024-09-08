from flask import Flask, render_template, request
from business import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
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