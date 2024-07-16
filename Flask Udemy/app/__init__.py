from flask import Flask  # importando a classe Flask do pacote flask
from flask_sqlalchemy import SQLAlchemy  # importando a classe SQLAlchemy do pacote flask_sqlalchemy banco de dados
from flask_migrate import Migrate  # importando a classe Migrate do pacote flask_migrate para migração do banco de dados

app = Flask(__name__)  # criando uma instância da classe Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'  # configurando o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # desabilitando o rastreamento de modificações

db = SQLAlchemy(app)  # criando uma instância da classe SQLAlchemy
migrate = Migrate(app, db)  # criando uma instância da classe Migrate


from app.views import homepage  # importando a views
from app.models import contato  # importando o model contato
