from sqlalchemy import create_engine, text
from flask import Flask,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# import os

# db_connection_string = os.environ['DB_CONNECTION_STRING']
# db_connection_string = 'mysql+mysqlconnector://root:159753@localhost/bddesafio3'

app=Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:123456789@dbdesafio5.cl64ekaqq8ka.us-east-1.rds.amazonaws.com:3306/dbdesafio5'
db = SQLAlchemy(app)


#variavel contendo o caminho para o banco de dados
db_connection_string = 'mysql+mysqlconnector://admin:123456789@dbdesafio5.cl64ekaqq8ka.us-east-1.rds.amazonaws.com:3306/dbdesafio5'

#conecta no banco de dados
engine = create_engine(
  db_connection_string)

#seleciona todas as pessoas
def pessoadb():
  with engine.connect() as conn:
    result = conn.execute(text("select * from pessoas"))
    pessoas = []
    for row in result.all():
      pessoas.append(row._asdict())
    return pessoas
  
#seleciona uma pessoa
def select_user(id):
  a=pessoadb()
  usuario= next((x for x in a if x['id']==int(id)),None) #função pra filtrar por id
  return usuario

# def teste(nome):
#   with engine.connect() as conn:
#     result = conn.execute(
#       text("SELECT * FROM jobs WHERE nome = :val"),val= nome)
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return dict(rows[0])
    


        
                #  nome=data['nome'],
                #  email=data['email'],
                #  funcao=data['funcao'],
                #  senha=data['senha'])