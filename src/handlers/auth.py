from flask import jsonify
from src.utils.passwordHash import hash_password
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
        db.session.commit()
        
        hased_password,salt = hash_password(password)

        user_password = UserPassword(user_id = user.id,
                                     hashed_password =hased_password,
                                     salt = salt )
        db.session.add(user_password)
        db.session.commit()

        response = {
            "body": {
                "message": "User registered successfully",
                "access_token": "test",
                "token_type": "bearer"
            }
        }
        status_code = 201

        return  jsonify(response), status_code