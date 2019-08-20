import logging

from flask import Flask, Blueprint

from api.blog.endpoints.posts import ns as blog_posts_namespace
from api.restplus import api

from database import db

log = logging.getLogger(__name__)
app = Flask(__name__)


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('demo flask api', __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


if __name__ == '__main__':
    initialize_app(app)
    log.info(">>> Starting the dev app at url http://{}/".format('localhost'))
    log.info(">>> App Name: %s " % app.name)
    app.run('localhost', '8081', debug=True)
