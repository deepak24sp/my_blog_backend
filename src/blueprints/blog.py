from flask.blueprints import Blueprint
from src.handlers import Blog
from flask import request
from src.utils.auth_utils import login_required

blueprints = Blueprint("blog",__name__)

@blueprints.route("/home",methods = ['GET'])
def home():
    return Blog(request = request).home()

@blueprints.route("/",methods= ['GET'])
def blog_by_id():
    blog_id  = request.args.get('id')
    if not blog_id:
        response ={ 
            "body": {
                "status": False,
                "error": "the Blog may be removed "
            } }
        return response
    return Blog(request=request).blog_by_id(blog_id)

@blueprints.route("/post",methods = ['POST'])
@login_required
def add_blog(user_id): 
    return Blog(request=request).add_blog(user_id=user_id)