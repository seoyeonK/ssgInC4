import json
import pymysql

def getConnection():
    return pymysql.connect(host="192.168.111.132", 
                     user="seoyeon", 
                     passwd="iloveyou7", 
                     db="test", charset="utf8")


# datetime을 포함한 데이터를 json으로 바로 바꿀 수 있도록 추가한 함수
def user_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

# name을 parameter로 받아 user 테이블에 추가
def createUser(user_info):
    #user_info :  name, ID, password, phoneNumber, rent
    conn = getConnection()
    curs = conn.cursor()
    ok = curs.execute("INSERT INTO User(name, ID, password, phoneNumber) VALUES (%s, %s, %s, %s)", 
                      (user_info[0], user_info[1], user_info[2], user_info[3]))
    
    conn.commit()
    conn.close()

    return json.dumps({'rows': ok})