from flask import Flask, request


def create_app(test_config=None):
    '''Create and configure an instance of the Flask'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        )


    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return "I'm okay dude"

    return app
