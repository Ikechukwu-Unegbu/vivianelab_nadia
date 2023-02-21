from flask import Blueprint, render_template, request, redirect, flash
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User
from ...Services import Helpers 
from werkzeug.security import generate_password_hash, check_password_hash


settings = Blueprint('settings', __name__, template_folder='templates', static_folder="static", static_url_path='/Settings/static')


@settings.route('/settings')
def govupload():
    return "settings"

@settings.route('/settings/notification')
def notification_settings():
    user = Helpers.get_user_type(current_user)
    if(user == 'therapist'):
        logged_user = Therapist.query.get(current_user.id)
    elif(user == 'user'):
        logged_user = User.query.get(current_user.id)
    else:
        logged_user = User.query.get(current_user.id)
    return render_template('notification_settings.html', logged_user = logged_user)




@settings.route('/settings/visibility')
def visibility_settings():
    return render_template('visibility_settings.html')

@settings.route('/settings/security')
def security_settings():
        user = Helpers.get_user_type(current_user)
        if(user == 'therapist'):
            logged_user = Therapist.query.get(current_user.id)
        elif(user == 'user'):
            logged_user = User.query.get(current_user.id)
        else:
            logged_user = User.query.get(current_user.id)
        
        return render_template('security_settings.html', logged_user=logged_user)


@settings.route('/settings/password-change', methods=["POST"])
def reset_password():
    # get inputs from html
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_new = request.form.get('confirm_new')
    if new_password != confirm_new: 
        flash("Password Mismatch!", "password")
        return redirect(request.referrer)
    # verify old password.
    # get user type
    user = Helpers.get_user_type(current_user)
    if user == 'user':
        user = User.query.get(current_user.id)
        # Generate a hash of the new password
        password_hash = generate_password_hash(new_password)
        # Update the user model's password field with the new hash
        user.password = password_hash
        # Save the user model to the database
        db.session.commit()
        # change password
    elif user == 'therapist':
        user = Therapist.query.get(current_user.id)
        # Generate a hash of the new password
        password_hash = generate_password_hash(new_password)
        # Update the user model's password field with the new hash
        user.password = password_hash
        # Save the user model to the database
        db.session.commit()
        # change password

    flash('Password successfully Changed.', 'password_success')
    return redirect(request.referrer)

@settings.route('/settings/misc', methods=["POST"])
def settings_misc():
    username = request.form.get('username')
    phone = request.form.get('phone')
    email = request.form.get('email')
    user = Helpers.get_user_type(current_user)
    if user == 'user':
        user = User.query.get(current_user.id)
        
        user.username = username
        user.phone = phone
        user.email = email       
        db.session.commit()
        # change password
    elif user == 'therapist':
        user = Therapist.query.get(current_user.id)
        user.username = username
        user.phone = phone
        user.email = email       
        db.session.commit()
        db.session.commit()
        # change password
    flash('Personal details successfully updated.', 'personal')
    return redirect(request.referrer)

@settings.route('/settings/payment')
def payment_settings():
    """
        This endpoint renders the html page for payment settings
    """
    return render_template('payment_settings.html')


@settings.route('/settings/verification')
def verification_settings():
    """
        This is web endpoint for verification settings page
    """

    return render_template('verification_settings.html')

@settings.route('/settings/verification/identity')
def settings_verification_identity():
    return render_template('verification_settings.html')

@settings.route('/settings/verification/crime')
def settings_verification_crime():
    return render_template('verification_settings.html')


@settings.route('/test-form')
def test_form():
    return render_template('form.html')