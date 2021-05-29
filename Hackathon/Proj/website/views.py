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