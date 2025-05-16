from flask.blueprints import Blueprint
from src.handlers import Auth
from flask import request
blueprints =  Blueprint("auth",__name__)

@blueprints.route("/register",methods = ['POST'])
def register():
    return Auth(request = request).register()