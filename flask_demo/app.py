import logging

from flask import Flask, Blueprint
from api.restplus import api


log = logging.getLogger(__name__)
app = Flask(__name__)


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix="/api")
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)


if __name__ == '__main__':
    initialize_app(app)
    log.info(">>> Starting the dev app at url http://{}/".format('localhost'))
    log.info(">>> App Name: %s " % app.name)
    app.run('localhost', '8081', debug=True)
