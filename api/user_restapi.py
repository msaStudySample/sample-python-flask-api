from flask import Blueprint, jsonify, request
from models import User
from extentions import ma, db
from models.user import UserSchema


api_v1 = Blueprint('API_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/users')
def list_users():
    from wsgi import app
    app.logger.info("users call")

    schema = UserSchema(many=True)
    all_Users = User.query
    result = dict()
    result['data'] = schema.dump(all_Users)
    return jsonify(result)


@api_v1.route('/user', methods=['POST'])
def create_user():
    schema = UserSchema()
    result = dict()

    req_data = request.get_json()
    if 'email' in req_data.keys():
        email = req_data['email']
        user = User.query.get(email)

        if user is None:
            user = User()
            user.email = req_data['email']
            if 'password' in req_data.keys():
                user.password = req_data['password']
            if 'name' in req_data.keys():
                user.name = req_data['name']
        else:
            #   TODO 존재하면 있다고 리턴
            result['msg'] = 'user exists'
            return jsonify(result), 400
    else:
        user = schema.load(request.json)

    db.session.add(user)
    db.session.commit()

    result['msg'] = "user created"
    result['data'] = schema.dump(user)

    return jsonify(result)


@api_v1.route('/user/<email>', methods=['GET'])
def get_user(email):
    schema = UserSchema()
    result = dict()

    user = User.query.get_or_404(email)

    result['msg'] = 'OK'
    result['data'] = schema.dump(user)

    return jsonify(result), 200


@api_v1.route('/put_user')
def put_user():
    schema = UserSchema()
    result = dict()

    if not request.is_json:
        result['msg'] = 'Missing JSON in request'
        return jsonify(result), 400

    req_data = request.get_json()

    if 'email' in req_data.keys():
        email = req_data['email']
        user = User.query.get_or_404(email)
        if 'password' in req_data.keys():
            user.password = req_data['password']
        if 'name' in req_data.keys():
            user.name = req_data['name']
        db.session.add(user)
        db.session.commit()
        result['msg'] = 'OK'
        result['data'] = schema.dump(user)
    else:
        result['msg'] = 'keys error'
        return jsonify(result), 400

    return jsonify(result), 200


@api_v1.route('/delete_user')
def delete_user():
    schema = UserSchema
    result = dict()

    if not request.is_json:
        result['msg'] = 'Missing JSON in request'
        return jsonify(result), 400

    email = request.json.get('email', None)
    user = User.query.get_or_404(email)
    db.session.delete(user)
    db.session.commit()

    result['msg'] = 'OK'
    result['data'] = schema.dump(user)
    return jsonify(result), 200









