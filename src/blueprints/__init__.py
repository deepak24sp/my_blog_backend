from src.blueprints import test
from src.blueprints  import auth 
from src.blueprints import blog
def init_blueprint(app):
    app.register_blueprint(auth.blueprints,url_prefix='/auth')
    app.register_blueprint(blog.blueprints,url_prefix='/blog')
    