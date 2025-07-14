from flask.blueprints import Blueprint
from src.handlers import Auth
from flask import request
blueprints =  Blueprint("auth",__name__)

@blueprints.route("/register",methods = ['POST'])
def register():
    return Auth(request = request).register()

@blueprints.route("/login",methods = ["POST"])
def login():
    return Auth(request=request).login()

@blueprints.route("/verify",methods = ['POST'])
def verify():
    return Auth(request=request).verify()