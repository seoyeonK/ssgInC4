from flask import Flask, render_template, request
from flask_restful import Resource,reqparse, Api
import utils.userdao as userdao
from utils.utils import hash_password

# 회원가입 : https://luvris2.tistory.com/196

app = Flask(__name__)
api = Api(app)

@app.route('/signup')
def display_user_signup_form():
    return render_template('signup.html')


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
        
        return userdao.createUser(user_info)
    
    except Exception as e :
        return {'error': str(e)}



@app.route('/')
def hello_world():
    return 'hello world!'