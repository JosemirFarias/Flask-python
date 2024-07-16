from app import db  # importando a instância do banco de dados
from datetime import datetime, timezone # importando a classe datetime do pacote datetime e a classe timezone do pacote timezone

class contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # criando uma coluna id do tipo inteiro e chave primária

    data_envio = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # criando uma coluna data_envio do tipo datetime com a data e hora atual em UTC
    
    nome = db.Column(db.String, nullable=False)  # criando uma coluna nome do tipo string não nula
    
    email = db.Column(db.String, nullable=False)  # criando uma coluna email do tipo string não nula
    
    assunto = db.Column(db.String, nullable=False)  # criando uma coluna assunto do tipo string não nula
    
    mensagem = db.Column(db.String, nullable=False)  # criando uma coluna mensagem do tipo string não nula