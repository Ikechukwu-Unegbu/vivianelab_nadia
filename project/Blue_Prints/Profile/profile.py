import os
from flask import Blueprint, render_template, request, redirect, flash, url_for, current_app, send_from_directory
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User
from ...models.Work import Work 
from ...models.Education import Education

profile = Blueprint('profile', __name__, template_folder='templates', static_folder="static", static_url_path='/profile/static')

@profile.route('/uploads/')
def uploaded_file():
    return send_from_directory(current_app.config['AVATAR_FOLDER'], 'alx.jpg')


@profile.route('/dashboard/my/')
@login_required
def myprofile():
    # make sure that given id is same as auth user id

    therapist = Therapist.query.filter_by(id=current_user.id).first()
    edu = Education.query.filter_by(therapist_id=current_user.id).all()
    work = Work.query.filter_by(therapist_id=current_user.id).all()

    return render_template('/profile/profile.html', therapist=therapist, work=work, edu=edu)

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

@profile.route('/add-work', methods=["POST"])
@login_required 
def add_work_history():
    employer = request.form.get('employer')
    title = request.form.get('job_title')
    description = request.form.get('description')
    starting_month = request.form.get('starting_month')
    starting_year = request.form.get('starting_year')
    ending_year = request.form.get('ending_year')
    ending_month = request.form.get('ending_month')
    # therapist = Therapist.q
    work = Work(
        employer=employer,
        jobrole=title,
        description=description,
        starting_month=starting_month,
        starting_year=starting_year,
        ending_month=ending_month,
        ending_year=ending_year,
        # created_at=datetime.utcnow(),
        therapist_id=current_user.id 
    )

    db.session.add(work)
    db.session.commit()
    referer = request.headers.get('Referer')
    return redirect(referer) 



@profile.route('/add-education', methods=["POST"])
@login_required 
def add_education_history():
    school = request.form.get('school')
    course = request.form.get('course')
    description = request.form.get('description')
    starting_month = request.form.get('starting_month')
    starting_year = request.form.get('starting_year')
    ending_year = request.form.get('ending_year')
    ending_month = request.form.get('ending_month')
    # therapist = Therapist.q
    edu = Education(
        school=school,
        course=course,
        description=description,
        starting_month=starting_month,
        starting_year=starting_year,
        ending_month=ending_month,
        ending_year=ending_year,
        # created_at=datetime.utcnow(),
        therapist_id=current_user.id 
    )

    db.session.add(edu)
    db.session.commit()
    referer = request.headers.get('Referer')
    return redirect(referer) 

