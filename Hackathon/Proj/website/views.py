from flask import Blueprint, app, render_template, redirect,request, jsonify, make_response
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home')
@login_required
def home():
    
    print(current_user)
    

    
    return render_template("index.html", user=current_user)

@views.route('/contacts')
@login_required
def contact():
    

    
    return render_template("contact.html", user=current_user)

@views.route('/upload')
@login_required
def upload():
    

    
    return render_template("upload.html", user=current_user)

@views.route('/download')
@login_required
def download():
    

    
    return render_template("download.html", user=current_user)