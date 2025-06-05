import jwt
from datetime import datetime, timedelta
from src.config import FlaskAppConfig

def generate_token(user_id, expires_in=3600):
    payload = {
        "user_id": user_id,
        "exp": datetime.now() + timedelta(seconds=expires_in),
        "iat": datetime.now()
    }
    token = jwt.encode(payload, FlaskAppConfig.SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, FlaskAppConfig, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
