from flask.blueprints import Blueprint

blueprint = Blueprint("test",__name__)

@blueprint.route("/",methods = ['GET'])
def test():
    return "testSuccessful"