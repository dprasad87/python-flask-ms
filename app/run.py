import sys
import logging
from api.configuration import configurations
from .api.bootstrap import init

configuration = configurations[sys.argv[1]]
api = init(configuration)
app = api.app

if __name__ == '__name__':
    try:
        app.run(threaded=True, use_reloader=False)
    except:
        logging.error