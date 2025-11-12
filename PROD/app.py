from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
       host="localhost",
       user="root",
       password="",
       database="produtos_db"
    )

@app.route('/')
def index():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    con.close()
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO produtos (nome, preco, quantidade) VALUE (%s, %s, %s)", (nome, preco, quantidade))
    con.commit()
    con.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)