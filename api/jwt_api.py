from flask import Blueprint, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, jwt_optional, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies,  get_jwt_identity, get_jwt_claims)
from wsgi import app
from models import User

app.config['JWT_SECRET_KEY'] = 'super-secrete'
jwt = JWTManager(app)

jwt_api_v1 = Blueprint('JWT_API_v1', __name__, url_prefix='/api/v1')


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    result = dict()
    result['email'] = identity
    result['subject'] = ['math', 'eng']
    return result
    # return {
    #     'name': identity,
    #     'subject': ['math', 'eng']
    # }


@jwt_api_v1.route('/login', methods=['POST'])
def login():
    from wsgi import bcrypt
    result = dict()
    if not request.is_json:
        result['msg'] = "Missing JSON in request"
        return jsonify(result), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.get(email)

    if user is None:
        result['msg'] = "Please check your email or password."
        return jsonify(result), 401
    else:
        # TODO checking password == hash password
        if not bcrypt.check_password_hash(user.password, password):
            result['msg'] = "Please check your email or password."
            return jsonify(result), 401

    # if email != 'test' or password != 'test':
    #     result['msg'] = "Bad username or password"
    #     return jsonify(result), 401

    # Create the tokens we will be sending back to the user
    access_token = create_access_token(email)
    refresh_token = create_refresh_token(email)

    # result['access_token'] = create_access_token(email)
    result['msg'] = "login success"
    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return jsonify(result, 200)


@jwt_api_v1.route('/get_email', methods=['GET'])
@jwt_required
def get_email():
    current_user = get_jwt_identity()
    return jsonify(name=current_user), 200


@jwt_api_v1.route('/call', methods=['GET'])
@jwt_required
def call():
    current_user = get_jwt_claims()
    result = dict()
    result['email'] = current_user['email']
    result['subject'] = current_user['subject']
    return jsonify(result, 200)
    # current_user = get_jwt_claims()
    # return jsonify({'name': current_user['name'], 'subject': current_user['subject']}), 200
