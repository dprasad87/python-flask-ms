import logging

from flask import Flask
from flask_restplus import Api, Resource
from api.restplus import api


log = logging.getLogger(__name__)
app = Flask(__name__)


# api = Api(app)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


if __name__ == '__main__':
    log.info(">>> Starting the dev app at url http://{}/".format('localhost'))
    log.info(">>> App Name: %s " % app.name)
    app.run('localhost', '8081', debug=True)
