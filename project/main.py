from flask import Blueprint, render_template, request, redirect
from . import db
from datetime import datetime
from flask_login import login_required, current_user
from .Services.Helpers import get_user_type
from .models.Appointment import Appointment
from .models.User import User
from .models.Locations.City import City
from .models.Locations.UserCity import UserCity
from .models.Notification import Notification

import random
from sqlalchemy import func

main = Blueprint('main', __name__, static_folder='static', static_url_path="/static")

@main.route('/')
def index():
    theras =  User.query.filter_by(access='THERAPIST').order_by(func.random()).limit(5).all()
    
    return render_template('home.html', theras=theras)

@main.route('/dashboard')
@login_required
def dashboard():
    
    # user_type = get_user_type(current_user)
    results = None
    future_appointments = Appointment.query.filter(
        Appointment.session_date > datetime.now().date(),
        Appointment.user_id == current_user.id
    ).order_by(Appointment.session_date).limit(10).all()

    if current_user.access == 'user' or current_user.access == "USER":
        return render_template('authenticated/user_dashboard.html', results=results, appointments=future_appointments)
    if current_user.access == 'therapist' or current_user.access =="THERAPIST":
        return render_template('authenticated/therapist_dashboard.html', results=results, appointments=future_appointments)


@main.route('/search-therapists/', methods=['POST', 'GET'])
# @login_required
def search_therapists_by_city():
    """
        This endpoint handles user/patient search for therapists accross cities
    """
    # get search term - city name
    city_name = request.args.get('city_name')
    # search the for such cities
    searched_cities = City.query.filter(City.name.like(f"%{city_name}%")).all()
    #If there are such cities - make array of their id
    if searched_cities:
        city_ids = [city.id for city in searched_cities]
        therapist_ids = []
        # get Id of therapists in those cities and save them in therapist_ids list
        for city_id in city_ids:
            city_users = UserCity.query.filter_by(city_id=city_id).all()
            therapist_ids += [city_user.user_id for city_user in city_users]

        if therapist_ids:
            # get profile of theses therapists
            therapists = User.query.filter(User.id.in_(therapist_ids)).all()
        else:
            therapists = []
        results = therapists
    else:
        
        results = None
    if current_user.is_authenticated:
        return render_template('authenticated/user_dashboard.html', results=results, cities=searched_cities)
    else: 
        return render_template('authenticated/user_dashboard.html', results=results, cities=searched_cities)

@main.route('/notifications')
def notifications():
    # get all his notifications and mark them as read.
    # notifications = Notification.query.filter_by(user_id=current_user.id, is_read=False).all()
    # for notification in notifications:
    #     notification.is_read = True
    #     db.session.commit()

    return render_template('pages/notifications/notifications.html')


