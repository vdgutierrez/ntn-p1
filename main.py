from flask import Flask, render_template, request
from business import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
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