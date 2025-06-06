from flask import jsonify
from src.db import db
from src.models.blog import Blog as BlogModel

class Blog:
    def __init__(self,request):
        self.request = request
    
    def home(self):
        blogs = db.session.query(BlogModel.id,BlogModel.title ,BlogModel.tags,BlogModel.user_id).limit(5).all()
        data = []
        for blog in blogs:
            data.append({
                "id":blog.id,
                "title":blog.title,
                "tags":blog.tags,
                "user_id":blog.user_id
            })
        response = {
            "body":{
                "status":True,
                "data":data
            }
        }
        return jsonify(response),200