from flask import jsonify
from src.db import db
from src.models.blog import Blog as BlogModel
from src.models.users import User 

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
            .limit(5)
            .all()
        )

        data = []
        for blog in blogs:
            data.append({
                "id": blog.id,
                "title": blog.title,
                "tags": blog.tags,
                "user_id": blog.user_id,
                "user_name": blog.user_display_name  # label matches above
            })

        response = {
            "body": {
                "status": True,
                "data": data
            }
        }
        return jsonify(response), 200
    
    def blog_by_id(self, id):
        try:
            # Query to fetch blog and its user's display name
            # result = (
            #     db.session.query(
            #         BlogModel,
            #         User.display_name.label("user_display_name")
            #     )
            #     .join(User, BlogModel.user_id == User.id)
            #     .filter(BlogModel.id == id)
            #     .first()
            # )
            result = (
                db.session.query(BlogModel,User).join(User).filter(BlogModel.id == id).first()
            )

            # If result is found, unpack and format the response
            print("QUERY RESULT:", result)
            if result:
                blog, user = result

                return jsonify({
                    "body": {
                        "status": True,
                        "blog": {
                            "id": blog.id,
                            "title": blog.title,
                            "tags": blog.tags,
                            "user_id": blog.user_id,
                            "content": blog.content,
                            "user_name": user.display_name
                        }
                    }
                }), 200

            # Blog not found
            return jsonify({
                "body": {
                    "status": False,
                    "error": f"Blog with id {id} not found"
                }
            }), 404

        except Exception as e:
            print(f"[ERROR] Exception in blog_by_id: {e}")
            return jsonify({
                "body": {
                    "status": False,
                    "error": "An unexpected error occurred while retrieving the blog."
                }
            }), 500
