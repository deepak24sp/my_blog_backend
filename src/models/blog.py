from src.db import db
from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.dialects.postgresql import JSON

class Blog(db.Model):
    __tablename__ = "blog"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(30),nullable=False)
    tags = Column(JSON, nullable=True)
    content = Column(Text,nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="blogs")
    