from flask import Flask

from blueprints import test
def create_app():
    app = Flask(__name__)

    app.register_blueprint(test.blueprint,url_prefix = '/test')

    
    return app