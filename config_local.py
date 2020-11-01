db = {
    'user'    : 'msa',
    'password': 'msa1234!',
    'host'    : 'localhost',
    'port'    : '3306',
    'database': 'msa'
}


SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SECRET_KEY = 'local key'
BCRYPT_LEVEL = 10

BASE_URL = 'http://127.0.0.1:8080'  

# JWT_SECRET_KEY = 'local-secret'
# JWT_TOKEN_LOCATION = ['cookies']
# JWT_ACCESS_TOKEN_EXPIRES = 1800
# JWT_COOKIE_SECURE = False
# JWT_REFRESH_TOKEN_EXPIRES = 15
# JWT_COOKIE_CSRF_PROTECT = True
# JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
# JWT_REFRESH_CSRF_HEADER_NAME = "X-CSRF-TOKEN-REFRESH"

JWT_SECRET_KEY = 'super-secret'
# JWT_COOKIE_SECURE = False # https를 통해서만 cookie가 갈 수 있는지 (production 에선 True)
# JWT_TOKEN_LOCATION = ['cookies']
# JWT_ACCESS_COOKIE_PATH = '/api/v1' # access cookie를 보관할 url (Frontend 기준)
# JWT_REFRESH_COOKIE_PATH = '/api/v1' # refresh cookie를 보관할 url (Frontend 기준)
# JWT_ACCESS_COOKIE_PATH = '/' # access cookie를 보관할 url (Frontend 기준)
# JWT_REFRESH_COOKIE_PATH = '/' # refresh cookie를 보관할 url (Frontend 기준)
# CSRF 토큰 역시 생성해서 쿠키에 저장할지
# (이 경우엔 프론트에서 접근해야하기 때문에 httponly가 아님)
# JWT_COOKIE_CSRF_PROTECT = False
# JWT_CSRF_CHECK_FORM = False
# JWT_ALGORITHM = 'HS256'
