import logging

from flask import Flask, Blueprint

from api.blog.endpoints.posts import ns as blog_posts_namespace
from api.restplus import api

from database import db

log = logging.getLogger(__name__)
application = Flask(__name__)


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


def create_app():
    initialize_app(application)
    return application

if __name__ == '__main__':
    initialize_app(application)
    log.info(">>> Starting the dev app at url http://{}/".format('localhost'))
    log.info(">>> App Name: %s " % application.name)
    application.run('localhost', '8081', debug=True)
