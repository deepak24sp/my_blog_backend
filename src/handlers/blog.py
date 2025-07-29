from flask import jsonify
from src.db import db
from src.models.blog import Blog as BlogModel
from src.models.users import User 
from src.utils.response import make_response

class Blog:
    def __init__(self, request):
        self.request = request

    def home(self):
        blogs = (
            db.session.query(
                BlogModel.id,
                BlogModel.title,
                BlogModel.tags,
                BlogModel.user_id,
                User.display_name.label("user_display_name")  
            )
            .join(User, BlogModel.user_id == User.id)
            .limit(10)
            .all()
        )

        data = []
        for blog in blogs:
            data.append({
                "id": blog.id,
                "title": blog.title,
                "tags": blog.tags,
                "user_id": blog.user_id,
                "user_name": blog.user_display_name 
            })

        return make_response(
            success=True,
            message="fetched the blog succesfully",
            data=data
        )
    
    def blog_by_id(self, id):
        try:
            result = (
                db.session.query(BlogModel,User).join(User).filter(BlogModel.id == id).first()
            )
            # print("QUERY RESULT:", result)
            if result:
                blog, user = result
                blog = {
                            "id": blog.id,
                            "title": blog.title,
                            "tags": blog.tags,
                            "user_id": blog.user_id,
                            "content": blog.content,
                            "user_name": user.display_name
                        }
                return make_response(
                    success=True,
                    message="succesfully fetched the blog",
                    data=blog
                )
            
            return make_response(
                success=False,
                message="blog not found",
                status_code= 404
                )


        except Exception as e:
            print(f"[ERROR] Exception in blog_by_id: {e}")
            return make_response(
                success=False,
                message="error occured while getting Blog",
                error="{e}",
                status_code=500
            )
        
    def add_blog(self,user_id):
        body = self.request.get_json()
        
        try:    
            blog = BlogModel(  
                title=body['title'],
                content=body['content'],
                tags=body.get('tags', []),
                user_id=user_id  
            )

            db.session.add(blog)
            db.session.commit()
            return make_response(
                success=True,
                message="successfully posted ",
                status_code=201
            )
        
        except Exception as e:
            print(f"[ERROR] Exception in blog_by_id: {e}")
            return make_response(
                success=False,
                message="error occured while getting Blog",
                error="{e}",
                status_code=500
            )