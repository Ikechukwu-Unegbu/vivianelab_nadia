import os
from flask import Blueprint, render_template, request, redirect, flash, url_for, current_app, send_from_directory
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User

profile = Blueprint('profile', __name__, template_folder='templates', static_folder="static", static_url_path='/profile/static')

@profile.route('/uploads/')
def uploaded_file():
    return send_from_directory(current_app.config['AVATAR_FOLDER'], 'alx.jpg')


@profile.route('/dashboard/my/')
@login_required
def myprofile():
    # make sure that given id is same as auth user id

    therapist = Therapist.query.filter_by(id=current_user.id).first()
    # get type instance of logged in user
    #  fetch user deatails from the right table

    return render_template('/profile/profile.html', therapist=therapist)

@profile.route('/update/bio-tagline', methods=["POST"])
@login_required
def update_bio_tagline():
    # Query the therapist with the given id
    therapist = Therapist.query.filter_by(id=current_user.id).first()

    # Update the therapist's tagline and bio
    therapist.tagline = request.form.get('tagline')
    therapist.bio = request.form.get('bio')

    # Commit the changes to the database
    db.session.commit()
    referer = request.headers.get('Referer')
    return redirect(referer) 

@profile.route('/avatar/upload', methods=["POST"])
@login_required
def upload_avatar():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Save the file to a folder on the server
            filename = file.filename
            file.save(os.path.join(profile.static_folder, 'uploads/avatar'+filename))
            #saving file to database 
            therapist = Therapist.query.filter_by(id=current_user.id).first()
            therapist.avatar = filename

            # Commit the changes to the database
            db.session.commit()
        
             
    referer = request.headers.get('Referer')
    return redirect(referer) 
