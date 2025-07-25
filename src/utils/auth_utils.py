from functools import wraps
import jwt
from flask import jsonify,request
from src.config import FlaskAppConfig


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({
                "status": False,
                "message": "Unauthorized: No token provided"
            }), 401

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, FlaskAppConfig.SECRET_KEY, algorithms=["HS256"])
            kwargs["user_id"] = payload['user_id']  
        except jwt.ExpiredSignatureError:
            return jsonify({
                "status": False,
                "message": "Token expired"
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                "status": False,
                "message": "Invalid token"
            }), 401
        
        return func(*args, **kwargs)
    return wrapper