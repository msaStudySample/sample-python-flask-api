db = {
    'user'    : 'msa',
    'password': 'msa1234!',
    'host'    : 'localhost',
    'port'    : '3306',
    'database': 'msa'
}


SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SECRET_KEY = 'development key'
