from app import create_app

application = create_app()


if __name__ == '__main__':
    # log.info(">>> Starting the dev app at url http://{}/".format('localhost'))
    # log.info(">>> App Name: %s " % application.name)
    application.run('localhost', '8081', debug=True)