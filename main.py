from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/question')
def question():
    return render_template('question.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/login_user', method=['POST'])
def login_user():
    print(request.method)
    if request.methods == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)

    return render_template('questions.html')
