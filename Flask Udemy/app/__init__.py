# importando a classe Flask do pacote flask
from flask import Flask

# criando uma instância da classe Flask
app = Flask(__name__)


# importando a views
from app.views import homepage