from flask import Flask  # importa a classe Flask do pacote flask

# inicialização
app = Flask(__name__)  # cria uma instância da classe Flask

# rota para a página inicial
@app.route('/')  # define a rota da
def ola_mundo(): # função que será executada ao acessar a rota
    return 'Olá, Mundo!' # retorna a string 'Olá, Mundo!'

# execurção da aplicação
app.run(debug=True)  # executa o servidor web