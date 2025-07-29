from flask import jsonify

def make_response(success=True, message="", data=None, status_code=200,error=False):
    return jsonify({
        "success": success,
        "message": message,
        "data": data,
        "error":error
    }), status_code
