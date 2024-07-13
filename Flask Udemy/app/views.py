# importando a aplicação 
from app import app

# importando a os arquivos dentro da pasta template 
from flask import render_template

# criando uma rota
@app.route('/')
def homepage():
    return render_template('index.html') # renderizando o arquivo index.html