from flask import Blueprint, jsonify, request
from models import User
from extentions import ma, db
from models.user import UserSchema

bp = Blueprint('user', __name__, url_prefix='/app')


@bp.route('/users')
def users():
    from wsgi import app
    app.logger.info("users call")

    schema = UserSchema(many=True)
    all_Users = User.query
    result = dict()
    result['data'] = schema.dump(all_Users)
    return jsonify(result)
