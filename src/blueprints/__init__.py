from src.blueprints import test

def init_blueprint(app):
    app.register_blueprint(test.blueprint,url_prefix='/')
    