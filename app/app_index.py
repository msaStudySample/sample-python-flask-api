from flask import Blueprint, jsonify

bp = Blueprint('idx', __name__, url_prefix='/')


@bp.route('/')
def idx():
    from wsgi import app
    app.logger.info("index call")

    results = dict()
    results['status'] = 'ok'

    return '''<!DOCTYPE HTML><html>
      <head>
        <title>Flask app</title>
      </head>
      <body>
        <h1>Hello Flask!</h1>
      </body>
    </html>'''
    # return jsonify(results)
