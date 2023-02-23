from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models.User import User
from .models.Therapist import Therapist

from flask_login import login_user, login_required, logout_user , current_user

auth = Blueprint('auth', __name__, static_folder="static", template_folder="templates", static_url_path="/protject/static")

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/therapist/login')
def therapist_login():
    return render_template('auth/therapist_login.html')

@auth.route('/therapist/login', methods=["POST"])
def therapist_login_post(): 
    email = request.form['email']
    password = request.form['password']
    therapist = Therapist.query.filter_by(email=email).first()
    if therapist and check_password_hash(therapist.password, password):
        login_user(therapist)
        return redirect(url_for('main.dashboard'))

    flash('Invalid email or password.')
    return redirect(url_for('auth.login'))




@auth.route('/login',methods=['POST'])
def login_post():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    user_def = request.form.get('user_def')
    email = request.form.get('email')
    password = request.form.get('password')
    if user_def == 'user':
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        
        if not check_password_hash(user.password, password):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))

        # return render_template('auth/login.html')
    elif user_def == 'therapist':
        therapist = Therapist.query.filter_by(email=email).first()
        if not therapist:
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
       
        if not check_password_hash(therapist.password, password):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(therapist)
        return redirect(url_for('main.dashboard'))
    flash('User not fond')
    return redirect(url_for('auth.login'))





@auth.route('/user/signup')
def signup():
    return render_template('auth/register.html')
@auth.route('/therapist/signup')
def therapist_signup():
    return render_template('auth/therapist_register.html')


@auth.route('/user/signup', methods=['POST'])
def signup_post():
  
       # code to validate and add user to database goes here
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    phone = request.form.get('phone')
    password = request.form.get('password')
  
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    username = User.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if username: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    new_user = User(email=email, fullname=fullname,username=username,phone=phone, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/therapist/signup', methods=['POST'])
def signup_therapist():
  
       # code to validate and add user to database goes here
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    phone = request.form.get('phone')
    password = request.form.get('password')
  
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    username = Therapist.query.filter_by(username=username).first() # if this returns a user, then the email already exists in database

    if username: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    new_user = Therapist(email=email, fullname=fullname,username=username,phone=phone, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

