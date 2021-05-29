from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import PickleType
from sqlalchemy.dialects.sqlite import BLOB
from flask import Flask, render_template, url_for

class Pdf(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    topics = db.Column(db.String(1000), default="None")
    no_of_upvotes = db.Column(db.Integer, default= 0)
    


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    
    pdf= db.relationship('Pdf', backref='author', lazy=True)