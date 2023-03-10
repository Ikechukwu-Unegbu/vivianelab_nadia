import os
from flask import Blueprint, render_template, request, redirect, flash, url_for, current_app, send_from_directory, jsonify
from datetime import datetime
from ...models.Locations.UserCity import UserCity
from ...models.Locations.City import City
from ...Services.Helpers import get_user_type
from ... import db
from flask_login import login_required, current_user

from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User
from ...models.Work import Work 
from ...models.Locations.Country import Country
from ...models.Education import Education
# from ...Services.Helpers ImportWarning

from jinja2 import Environment

profile = Blueprint('profile', __name__, template_folder='templates', static_folder="static", static_url_path='/profile/static')





@profile.route('/dashboard/my/')
@login_required
def myprofile():
    """
        This endpoint renders the logged in medic's profile. If user
        tries to access it when not logged  in Flask will direct the user to login.
    """
    # make sure that given id is same as auth user id
    if current_user.access == 'user' or current_user.access == 'USER':
        return redirect(url_for('main.dashboard'))

    therapist = User.query.filter_by(id=current_user.id).first()
    edu = Education.query.filter_by(therapist_id=current_user.id).all()
    work = Work.query.filter_by(therapist_id=current_user.id).all()
    country = Country.query.all()

    return render_template('/profile/profile.html', therapist=therapist, work=work, edu=edu, country=country, therapist_id=current_user.id)



@profile.route('/update/bio-tagline', methods=["POST"])
@login_required
def update_bio_tagline():
    """
    Endpoint to update bio, name and tagline on the web.
    """
    # Query the therapist with the given id
    therapist = User.query.filter_by(id=current_user.id).first()

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
    """
    This endpoint uploads new profile images from profile.
    """
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
            therapist = User.query.filter_by(id=current_user.id).first()
            therapist.avatar = filename

            # Commit the changes to the database
            db.session.commit()
        
             
    referer = request.headers.get('Referer')
    return redirect(referer) 

@profile.route('/add-work', methods=["POST"])
@login_required 
def add_work_history():
    """
    End point to add work history for users and medics.
    """
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


@profile.route('/edit-work/<int:id>', methods=["POST"])
@login_required 
def edit_work_history(id):
    """
       Endpoint for updating existing work history 
    """
    employer = request.form.get('employer')
    title = request.form.get('job_title')
    description = request.form.get('description')
    starting_month = request.form.get('starting_month')
    starting_year = request.form.get('starting_year')
    ending_year = request.form.get('ending_year')
    ending_month = request.form.get('ending_month')
    # therapist = Therapist.q
    work = Work.query.get(id)
    work.employer=employer
    work.jobrole=title
    work.description=description
    work.starting_month=starting_month
    work.starting_year=starting_year
    work.ending_month=ending_month
    work.ending_year=ending_year
 

    # db.session.add(work)
    db.session.commit()
    referer = request.headers.get('Referer')
    return redirect(referer) 






@profile.route('/add-education', methods=["POST"])
@login_required 
def add_education_history():
    """
        Endpoint to add new school or education history.
    """
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





@profile.route('/edit-education/<int:id>', methods=["POST"])
@login_required 
def edit_education_history(id):
    """
    Endpoint to edit existing work history.
    """
    school = request.form.get('school')
    course = request.form.get('course')
    description = request.form.get('description')
    starting_month = request.form.get('starting_month')
    starting_year = request.form.get('starting_year')
    ending_year = request.form.get('ending_year')
    ending_month = request.form.get('ending_month')
    # therapist = Therapist.q
    edu = Education.query.get(id)
    edu.school = school
    edu.course = course
    edu.description = description
    edu.starting_month = starting_month
    edu.starting_year = starting_year
    edu.ending_year = ending_year
    edu.ending_month = ending_month

    # db.session.update(edu)
    db.session.commit()
    referer = request.headers.get('Referer')
    return redirect(referer) 



@profile.route('/delete-work/<id>')
@login_required
def delete_work(id):
    """
    endpoint to delete work history
    """
    # find the record you want to delete
    work = Work.query.get(id)

# if the record exists, delete it
    if work:
        db.session.delete(work)
        db.session.commit()
    return redirect(request.referrer)

@profile.route('/delete-education/<id>')
@login_required
def delete_education(id):
    """
    Endpoint to delete education history
    """
    # find the record you want to delete
    edu = Education.query.get(id)

# if the record exists, delete it
    if edu:
        db.session.delete(edu)
        db.session.commit()
    return redirect(request.referrer)


@profile.route('/add-cities', methods=['POST'])
@login_required
def add_cities():
    """
    Endpoint to add city of residence.
    """
    # get the submitted city IDs as an array
    city_ids = request.json.get('city_ids')
    # get the model of the logged-in user
    # add each city ID as a record in the UserCity model for the logged-in user
    for city_id in city_ids:
        user_city = UserCity(user_id=current_user.id, city_id=city_id, user_model='user', created_at=datetime.now())
        db.session.add(user_city)

    db.session.commit()

    return jsonify({'success': True}), 200


@profile.route('/get-therapist-cities/<int:id>')
def get_therapist_cities(id):
    """
    this endpoint gets therapists who operate in city with given id
    """
    if current_user.is_authenticated:
        # Query UserCity model to get all rows where user_id = current user's id and user_model is therapist
        user_cities = UserCity.query.filter_by(user_id=id).all()

        # Query City model to get the city where id = city_id in each UserCity row
        cities = [City.query.get(user_city.city_id) for user_city in user_cities]

        # Return list of city names
        city_data = [{'id': city.id, 'name': city.name} for city in cities]
        return {'cities': city_data}
    else:
        return {'message': 'User not authenticated'}
    


@profile.route('/therapist/<int:id>')
def pub_therapist_profile(id):
   # make sure that given id is same as auth user id

    therapist = User.query.filter_by(id=id).first()
    edu = Education.query.filter_by(therapist_id=id).all()
    # location = UserCity.query.filter_by(therapist_id=id).all()
    work = Work.query.filter_by(therapist_id=id).all()
    country = Country.query.all()


     # Query UserCity model to get all rows where user_id = current user's id and user_model is therapist
    user_cities = UserCity.query.filter_by(user_id=id).all()

    # Query City model to get the city where id = city_id in each UserCity row
    cities = [City.query.get(user_city.city_id) for user_city in user_cities]

    # Return list of city names
    city_data = [{'id': city.id, 'name': city.name} for city in cities]

    return render_template('/profile/profile.html', therapist=therapist, work=work, edu=edu, country=country, therapist_id=id, cities=city_data)


