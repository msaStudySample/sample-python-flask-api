from flask import Flask, Blueprint, jsonify, request
from sqlalchemy import create_engine, text
from extentions import db
import os
from flask_cors import CORS

# bp = Blueprint('idx', __name__, url_prefix='/')


def create_app():
    application = Flask(__name__)
    if os.environ.get('APP_ENV') == 'prod':
        print('prod')
        application.config.from_object('config')
    elif os.environ.get('APP_ENV') == 'dev':
        print('dev')
        application.config.from_object('config_dev')
    else:
        print('local')
        application.config.from_object('config_local')

    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    application.secret_key = 'samplewithflask'

    CORS(application, supports_credentials=True)
    configure_extensions(application)

    database = create_engine(application.config['DB_URL'], encoding='utf-8')
    application.database = database

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

from app import app_index, user_restapi


app.register_blueprint(app_index.bp)
app.add_url_rule('/', endpoint='idx')
app.register_blueprint(user_restapi.bp)
app.add_url_rule('/', endpoint='user')


if __name__ == '__main__':
    app.run(port=8080)
