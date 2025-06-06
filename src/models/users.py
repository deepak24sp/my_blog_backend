from src.db import db
from sqlalchemy import Column,Integer,String

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    display_name = Column(String(30),nullable=True)
    username_name = Column(String(30),unique=True,nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = db.relationship("UserPassword", back_populates="user", uselist=False)
    blogs = db.relationship("Blog", back_populates="user", cascade="all, delete-orphan")