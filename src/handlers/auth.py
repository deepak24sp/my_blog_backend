from flask import jsonify
from src.utils.passwordHash import hash_password,verify_password
from src.utils.jwt_handler import generate_token,verify_token
from src.db import db
from src.models.users import User
from src.models.user_password import UserPassword
class Auth:
    def __init__(self,request):
        self.request = request
        
    def register(self):
        data = self.request.get_json()

        display_name = data.get('display_name')
        username_name = data.get('username_name')
        email = data.get('email')
        password = data.get('password')

        user = User(
                    display_name=display_name,
                    username_name=username_name,
                    email=email
                    )

        db.session.add(user)
        db.session.flush()
        
        hased_password,salt = hash_password(password)

        user_password = UserPassword(user_id = user.id,
                                     hashed_password =hased_password,
                                     salt = salt )
        db.session.add(user_password)
        db.session.commit()

        access_token = generate_token(user_id=user.id)

        response = {
            "body": {
                "message": "User registered successfully",
                "access_token": access_token,
                "token_type": "bearer"
            }
        }
        status_code = 201

        return  jsonify(response), status_code
    
    def login(self):
        data = self.request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"message": "Invalid email or password"}), 401

        user_password = UserPassword.query.filter_by(user_id=user.id).first()
        if not user_password:
            return jsonify({"message": "Password not set for user"}), 401

        if not verify_password(password, user_password.hashed_password, user_password.salt):
            return jsonify({"message": "Invalid email or password"}), 401

        token = generate_token(user.id)

        response = {
            "body": {
                "status":True,
                "message": "Login successful",
                "access_token": token,
                "token_type": "bearer"
            }
        }
        return jsonify(response), 200
    
    def verify(self):
        token = self.request.get_json()
        user = verify_token(token)
        if user:
            user_id = user.user_id
            user = db.session.query(User).filter(id = user_id).first()
            response = {
            "body": {
                "status":True,
                "message": "Login successful",
                "user_id":user_id,
                "user_name":user.username_name,
                "display_name":user.display_name
            }
        }
        return jsonify(response), 200
            
        return None