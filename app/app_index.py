from flask import Blueprint, jsonify, render_template

bp = Blueprint('idx', __name__, url_prefix='/')


@bp.route('/')
def idx():
    from wsgi import app
    app.logger.info("index call")

    results = dict()
    results['status'] = 'ok'
    return jsonify(results)
