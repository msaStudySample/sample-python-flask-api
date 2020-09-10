from flask import Blueprint, jsonify, request
from models import User
from extentions import ma, db
from models.user import UserSchema

api_v1 = Blueprint('API_v1', __name__, url_prefix='/api')


@api_v1.route('/v1/users')
def list_users():
    from wsgi import app
    app.logger.info("users call")

    schema = UserSchema(many=True)
    all_Users = User.query
    result = dict()
    result['data'] = schema.dump(all_Users)
    return jsonify(result)


@api_v1.route('/v1/user', methods=['POST'])
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
            return jsonify(result)
    else:
        user = schema.load(request.json)

    db.session.add(user)
    db.session.commit()

    result['msg'] = "user created"
    result['data'] = schema.dump(user)

    return jsonify(result)
