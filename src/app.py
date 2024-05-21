from flask import Flask,render_template, request , Response,jsonify,make_response,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text,create_engine
from crud import pessoadb,select_user
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask("__name__")
app.secret_key = '_5#y2L"F4dasQ8dasdasc]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://admin:123456789@dbdesafio5.cl64ekaqq8ka.us-east-1.rds.amazonaws.com:3306/dbdesafio5'
#variavel contendo o caminho para o banco de dados
db_connection_string = 'mysql+mysqlconnector://admin:123456789@dbdesafio5.cl64ekaqq8ka.us-east-1.rds.amazonaws.com:3306/dbdesafio5'

#conecta no banco de dados
engine = create_engine(
  db_connection_string)

db=SQLAlchemy(app)

class pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True,nullable=False)
    funcao = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(300),nullable=False)
    nota = db.Column(db.Integer,nullable=False)

    # def __init__(self,email,password,nome):
    #     self.nome = nome
    #     self.email = email
    #     self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # def check_password(self,password):
    #     return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zale')
def zale():
    return render_template('zale.html')


@app.route('/valere')
def valere():
    return render_template('valere.html')

@app.route('/oracle')
def oracle():
    return render_template('oracle.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

# @app.route('/usuario')
# def usuario():
#     user= pessoadb()

#     return render_template('user.html', user=user)

@app.route('/user',methods=['POST','GET'])
def user():
   
    data= request.form
    
    if  cadastro(data) == False:
        flash('EMAIL ALREADY EXISTS',category='error')
        return render_template('registro.html')
    else:
        flash('Sucessfuly registered!',category='success')
        return render_template('user.html', data=data)

#seleciona usuário pelo id
@app.route('/user/<id>')
def select(id):
    user=select_user(id)
    return render_template('user.html',data=user)


#Login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = pessoas.query.filter_by(email=email).first()
        
        if check_password_hash(user.password,password):
            session['email'] = user.email
            return render_template('/user.html',data=user)
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

def cadastro(data):
  with engine.connect() as conn:
    user= pessoas.query.filter_by(email=data['email']).first()
    if user:
      return False
    else:
      conn.execute(text(f"INSERT INTO pessoas( nome, email, funcao, password, nota) VALUES ( '{data['nome']}', '{data['email']}', '{data['funcao']}', '{generate_password_hash(data['password'],method='pbkdf2',salt_length=16)}','{data['nota']}')"))
    
      conn.commit()

if __name__==__main__:
    app.run()