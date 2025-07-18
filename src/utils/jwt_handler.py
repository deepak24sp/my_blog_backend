import jwt
from datetime import datetime, timedelta
from src.config import FlaskAppConfig

def generate_token(user_id, expires_in=3600):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(seconds=expires_in),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, FlaskAppConfig.SECRET_KEY, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, FlaskAppConfig.SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id")  
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
        print("JWT error:", str(e))
        return None

