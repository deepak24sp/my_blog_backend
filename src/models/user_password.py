from src.db import db
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class UserPassword(db.Model):
    __tablename__ = "user_passwords"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    salt = Column(String(64), nullable=False)

    user = relationship("User", back_populates="password")