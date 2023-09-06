from flask import Flask, render_template, request, redirect, flash, url_for
from flask_restful import Resource,reqparse, Api
import utils.userdao as userdao
import utils.utils as utils
from flask_cors import CORS

# 회원가입 : https://luvris2.tistory.com/196

app = Flask(__name__)
api = Api(app)
app.secret_key = "super secret key"

CORS(app)

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

@app.route('/signup_fail')
def signup_fail():
    return render_template('signup_fail.html')

@app.route('/signup', methods=['POST'])
def createUser():
    try:
        parser = reqparse.RequestParser()

        name = str(request.form.get('name'))
        ID = str(request.form.get('ID'))
        password = str(request.form.get('password'))
        phoneNumber = str(request.form.get('phoneNumber'))

        password_confirm = str(request.form.get('password_confirm'))
        
        # args = parser.parse_args()

        if len(ID) < 4 or len(ID) > 16 or not utils.onlyalpha(ID) or not phoneNumber.isdecimal() or not name.isalpha() or password != password_confirm:
           return redirect(url_for('signup_fail'))


        hashed_password = utils.hash_password(str(password))

        user_info = [ name , ID , hashed_password, phoneNumber ]
        
        a = userdao.createUser(user_info)

        return redirect(url_for('signup_complete'))
    
    except Exception as e :
        return {'error': str(e)}


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, threaded=True)