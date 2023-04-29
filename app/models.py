from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func
# from datetime import datetime
# from sqlalchemy import Integer, ForeignKey, String, Column
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(UserMixin, Base):
    __tablename__ = 'users'
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    phone = db.Column(db.Integer, unique=True)
    h_no = db.Column(db.String(10))
    address2 = db.Column(db.String(200))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    pincode = db.Column(db.Integer)
    github = db.Column(db.String(80), unique=True)
    linkedin = db.Column(db.String(80), unique=True)
    instagram = db.Column(db.String(80), unique=True)
    twitter = db.Column(db.String(80), unique=True)
    image_file = db.Column(db.String(20))


    project = db.relationship("Project", back_populates="author")

class Project(Base):
    __tablename__ = 'projects'
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship("User", back_populates="project")
    description = db.Column(db.String(200), unique=True, nullable=False)
    image_file = db.Column(db.String(20))
    link = db.Column(db.String(80), unique=True, nullable=False)
    github = db.Column(db.String(80), unique=True, nullable=False)
