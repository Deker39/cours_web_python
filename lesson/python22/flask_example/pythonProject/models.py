from flask_login import UserMixin
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    username = Column(String(50))
    password = Column(String(50))
