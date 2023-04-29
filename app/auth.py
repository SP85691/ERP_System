from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
import os
from . import db

auth = Blueprint("auth", __name__)

email_sender = 's.pratap.4155@gmail.com'
email_password = os.environ.get('Mail_Auth_Pass')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        
        login_user(user)

    return redirect(url_for('main.dashboard'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user exits
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # add user to database
        new_user = User(username=username, name=name, email=email, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()
        db.session.close()

    return redirect(url_for('auth.login'))

# Edit profile
@auth.route('/Update_profile')
@login_required
def edit_profile():
    return render_template('dashboard/content/edit_profile.html', 
                           name=current_user.name, 
                           email=current_user.email, 
                           username=current_user.username,
                           created_at=current_user.created_at
                           )


@auth.route("/Update_profile", methods=['GET', 'POST'])
@login_required
def edit_profile_post():

    if request.method == 'POST':
        if current_user.email == request.form.get('email'):

            current_user.name = request.form.get('name')
            current_user.username = request.form.get('username')
            current_user.h_no = request.form.get('h_no.')

            # update data
            

            db.session.commit()
            db.session.close()
            return redirect(url_for('main.about'))
        else:
            flash('Email address already exists')
            return redirect(url_for('auth.edit_profile'))
        
    return render_template('auth.edit_profile')


# @auth.route('/Update_profile', methods=['POST'])
# @login_required
# def edit_profile_post():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         name = request.form.get('name')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         h_no = request.form.get('h_no')
#         city = request.form.get('city')
#         state = request.form.get('state')
#         pincode = request.form.get('pincode')

#         # update data of current user
#         current_user.username = username
#         current_user.name = name
#         current_user.email = email
#         current_user.h_no = h_no
#         current_user.city = city
#         current_user.state = state
#         current_user.pincode = pincode
        
#         db.session.commit()
#         db.session.close()

#     return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')