from flask import Flask, request
from sqlalchemy import create_engine, text
from extentions import db
import os
from flask_cors import CORS
from flask_bcrypt import Bcrypt

# bp = Blueprint('idx', __name__, url_prefix='/')


def create_app():
    application = Flask(__name__)
    if os.environ.get('APP_ENV') == 'prod':
        print('prod')
        application.config.from_object('config_prod')
    elif os.environ.get('APP_ENV') == 'dev':
        print('dev')
        application.config.from_object('config_dev')
    else:
        print('local')
        application.config.from_object('config_local')
        print("SECRET_KEY : ", application.config.get("SECRET_KEY"))

    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # application.secret_key = 'samplewithflask'

    CORS(application, supports_credentials=True)
    configure_extensions(application)

    # TODO DB Pool 설정
    database = create_engine(application.config['DB_URL'], encoding='utf-8')
    application.database = database


    CORS(application, supports_credentials=True)

    @application.route('/sign-up', methods=['POST'])
    def sign_up():
        user = request.json
        user_id = app.database.execute(text("""
                                            INSERT INTO user(
                                                email,
                                                password
                                            ) VALUE (
                                                :email,
                                                :password
                                            )
                                            """), user).lastrowid
        return "OK", 200
    return application


def configure_extensions(app):
    db.init_app(app)


app = create_app()

from app import app_index
from api import user_restapi, jwt_api

app.register_blueprint(app_index.bp)
app.add_url_rule('/', endpoint='idx')
app.register_blueprint(user_restapi.api_v1)
app.add_url_rule('/', endpoint='API_v1')
app.register_blueprint(jwt_api.jwt_api_v1)
app.add_url_rule('/', endpoint='JWT_API_v1')

# app.config['SECRET_KEY'] = 'I love you!'
# app.config['BCRYPT_LEVEL'] = 10
print("SECRET_KEY : ", app.config.get("SECRET_KEY"))
print("BCRYPT_LEVEL : ", app.config.get("BCRYPT_LEVEL"))
# TODO create_app() 안에서 encryption이 좋을지 확인
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(port=8080)
