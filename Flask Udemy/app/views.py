# importando a aplicação 
from app import app

# importando a os arquivos dentro da pasta template 
from flask import render_template, url_for # render_template é responsável por renderizar o arquivo html e o url_for é responsável por criar links das rotas

# criando uma rota
@app.route('/')
def homepage():
    usuario = 'Josemir'
    idade = 34

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context) # renderizando o arquivo index.html

@app.route('/sobre')
def sobre():
    return render_template('sobre.html') # renderizando o arquivo sobre.html