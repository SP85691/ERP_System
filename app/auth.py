from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

# @auth.route('/login', methods=['POST'])
# def login_post():
#     return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user exits
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # add user to database
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return render_template('logout.html')