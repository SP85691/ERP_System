from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
@login_required
def about():
    return render_template('dashboard/content/about.html', 
                           name=current_user.name, 
                           email=current_user.email, 
                           username=current_user.username)