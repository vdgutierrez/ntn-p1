from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/landing/index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/login_user', methods=['POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        print(password)
    return 'received'













if __name__ == '__main__':
    app.run(debug=True)