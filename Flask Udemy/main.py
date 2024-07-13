# importando a aplicação 
from app import app

# rodando a aplicação o debug=True faz com que a aplicação seja reiniciada automaticamente, e usar o python main.py para rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)