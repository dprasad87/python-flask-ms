import logging

from flask import Flask
from flask_restplus import Api

def init(configuration):
    logging.info("Application running with {} configuration".format(configuration.__class__.__name__))
    api = Api(Flask(configuration.NAME))

    api.app.config.from_object(configuration)
    return api
