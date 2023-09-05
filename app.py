from flask import Flask, render_template, request, redirect, flash, url_for
from flask_restful import Resource,reqparse, Api
import utils.userdao as userdao
from utils.utils import hash_password

# 회원가입 : https://luvris2.tistory.com/196

app = Flask(__name__)
api = Api(app)
app.secret_key = "super secret key"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index_login')
def index_login():
    return render_template('index_login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html')

@app.route('/withdrawl')
def withdrawl():
    return render_template('withdrawl.html')

@app.route('/signup_complete')
def signup_complete():
    return render_template('signup_complete.html')


@app.route('/signup', methods=['POST'])
def createUser():
    try:
        parser = reqparse.RequestParser()

        name = request.form.get('name') 
        ID = request.form.get('ID')
        password = request.form.get('password')
        phoneNumber = request.form.get('phoneNumber')

        # password = request.form.get('password'
        
        args = parser.parse_args()

        # if len(data['password']) < 4 or len(data['password']) > 12 :
        #    return { "error" : "비밀번호의 길이를 확인해주세요 (4-12자리)" }, 400


        hashed_password = hash_password(str(password))

        user_info = [ str(name) , str(ID) , hashed_password, str(phoneNumber) ]
        
        a = userdao.createUser(user_info)

        return redirect(url_for('signup_complete'))
    
    except Exception as e :
        return {'error': str(e)}



@app.route('/')
def hello_world():
    return 'hello world!'