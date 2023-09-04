from flask import Flask
from flask_restful import Resource,reqparse, Api
import utils.userdao as userdao
from utils.utils import hash_password

# 회원가입 : https://luvris2.tistory.com/196

app = Flask(__name__)
api = Api(app)
@app.route('/user', methods=['POST'])
def createUser():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str, help='name cannot be blank')
        parser.add_argument('ID', required=True, type=str, help='ID cannot be blank')
        parser.add_argument('password', required=True, type=str, help='password cannot be blank')
        parser.add_argument('phoneNumber', required=True, type=str, help='ID cannot be blank')
        parser.add_argument('rent', required=False, type=str)
        args = parser.parse_args()

        # if len(data['password']) < 4 or len(data['password']) > 12 :
        #    return { "error" : "비밀번호의 길이를 확인해주세요 (4-12자리)" }, 400


        hashed_password = hash_password(str(args['password']))

        user_info = [ str(args['name']) , str(args['ID']) ,hashed_password, str(args['phoneNumber']), str(args['phoneNumber']) ]
        return userdao.createUser(user_info)
    
    except Exception as e :
        return {'error': str(e)}



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'hello world!'

    return app