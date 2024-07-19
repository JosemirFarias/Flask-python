# importando a aplicação 
from app import app

# importando a os arquivos dentro da pasta template 
from flask import render_template, url_for, request  # render_template é responsável por renderizar o arquivo html / url_for é responsável por criar links das rotas / request é responsável por pegar os dados do formulário


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

@app.route('/contato', methods=['POST'])  # criando uma rota para a página de contato
def contato():
    context = {}  # criando um dicionário vazio
    if request.method == 'POST':  # verificando se o método é POST
        pesquisa = request.form.get('pesquisa')  # pegando o valor do input com o name pesquisa
        print(pesquisa)  # imprimindo o valor do input
        context.update({'pesquisa': pesquisa})  # atualizando o dicionário com o valor do input
   
    return render_template('contato.html', context=context)  # renderizando o arquivo contato.html com o dicionário context