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
    data = db.Column(db.PickleType, nullable=True)
    no_of_likes = db.Column(db.Integer, default= 0)
    


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    
    pdf= db.relationship('Pdf', backref='author', lazy=True)