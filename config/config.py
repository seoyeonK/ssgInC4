class Config :
    # 암호화 키
    JWT_SECRET_KEY = 'ssg12345678asdlkjfq,mzdjdddfd' # 주의 : 노출되면 절대 안됨
    JWT_ACCESS_TOKEN_EXPIRES = True # 토큰 유지 시간
    PROPAGATE_EXCEPTIONS = True # 예외처리를 JWT로 처리