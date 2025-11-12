from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "chave_secreta"

# Conexão com o banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # coloque a senha do seu MySQL se tiver
        database="produtos_db"
    )

# ------------------ ROTAS -------------------

# Tela de login
@app.route('/')
def index():
    return render_template('index.html')

# Login
@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios WHERE login=%s AND senha=%s", (login, senha))
    usuario = cur.fetchone()
    con.close()

    if usuario:
        session['usuario'] = login
        return redirect('/classificacao')
    else:
        flash("Usuário ou senha incorretos!")
        return redirect('/')

# Cadastro de novo usuário
@app.route('/registrar', methods=['POST'])
def registrar():
    novo_login = request.form['novo_login']
    nova_senha = request.form['nova_senha']

    con = conectar()
    cur = con.cursor()

    # Evita duplicados
    cur.execute("SELECT * FROM usuarios WHERE login=%s", (novo_login,))
    existente = cur.fetchone()

    if existente:
        flash("Esse login já existe. Tente outro.")
    else:
        cur.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", (novo_login, nova_senha))
        con.commit()
        flash("Usuário cadastrado com sucesso! Agora você pode fazer login.")
    
    con.close()
    return redirect('/')

# Página de produtos
@app.route('/classificacao')
def classificacao():
    if 'usuario' not in session:
        return redirect('/')
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    con.close()
    return render_template('classificacao.html', produtos=produtos)

# Página de cadastro de produto
@app.route('/cadastro')
def cadastro():
    if 'usuario' not in session:
        return redirect('/')
    return render_template('cadastro.html')

# Salvar produto
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)", (nome, preco, quantidade))
    con.commit()
    con.close()
    return redirect('/classificacao')

# Logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)