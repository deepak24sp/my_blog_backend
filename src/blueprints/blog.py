from flask.blueprints import Blueprint
from src.handlers import Blog
from flask import request
blueprints = Blueprint("blog",__name__)

@blueprints.route("/home",methods = ['GET'])
def home():
    return Blog(request = request).home()