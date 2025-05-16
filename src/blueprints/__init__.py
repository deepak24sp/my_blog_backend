from src.blueprints import test
from src.blueprints  import auth 
def init_blueprint(app):
    app.register_blueprint(auth.blueprints,url_prefix='/auth')
    