# importando a aplicação 
from app import app

# importando a os arquivos dentro da pasta template 
from flask import render_template, url_for # render_template é responsável por renderizar o arquivo html e o url_for é responsável por criar links das rotas


@app.route('/')  # criando uma rota para a página inicial
def homepage():
    usuario = 'Josemir'
    idade = 34

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context) # renderizando o arquivo index.html

@app.route('/sobre') # criando uma rota para a página sobre
def sobre():
    return render_template('sobre.html') # renderizando o arquivo sobre.html

@app.route('/contato')  # criando uma rota para a página de contato
def contato():
    return render_template('contato.html')