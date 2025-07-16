from flask.blueprints import Blueprint
from src.handlers import Blog
from flask import request
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
                "error": "id argumnet is missing"
            } }
        return response
    return Blog(request=request).blog_by_id(blog_id)
    