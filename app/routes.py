from app import app
from flask import request, render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']
    return f'Você entrou com o e-mail: {email}'

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    return f'Conta criada com sucesso para: {nome} ({email})'

