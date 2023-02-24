from flask import Blueprint, render_template, request, redirect
from . import db
from flask_login import login_required, current_user
from .Services.Helpers import get_user_type
from .models.Therapist import Therapist
from .models.User import User
from .models.Locations.City import City
from .models.Locations.UserCity import UserCity

main = Blueprint('main', __name__, static_folder='static', static_url_path="/static")

@main.route('/')
def index():
    theras = Therapist.query.limit(4).all()
    if len(theras) < 4:
        theras = Therapist.query.all()
        # return therapists  
    return render_template('home.html', theras=theras)

@main.route('/dashboard')
@login_required
def dashboard():
    print(current_user)
    user_type = get_user_type(current_user)
    results = None
    if user_type == 'user':
        return render_template('authenticated/user_dashboard.html', results=results)
    if user_type == 'therapist':
        return render_template('authenticated/therapist_dashboard.html', results=results)


@main.route('/search-therapists/', methods=['POST', 'GET'])
@login_required
def search_therapists_by_city():
    # city_name = request.form['city_name']
    city_name = request.args.get('city_name')
    searched_cities = City.query.filter(City.name.like(f"%{city_name}%")).all()
    # searched_cities = City.query.filter(City.name.like(f"%{city_name}%")).all()
    if searched_cities:
        city_ids = [city.id for city in searched_cities]
        therapist_ids = []
        for city_id in city_ids:
            city_users = UserCity.query.filter_by(city_id=city_id, user_model="therapist").all()
            therapist_ids += [city_user.user_id for city_user in city_users]

        if therapist_ids:
            therapists = Therapist.query.filter(Therapist.id.in_(therapist_ids)).all()
        else:
            therapists = []
        results = therapists
    else:
        results = None
    return render_template('authenticated/user_dashboard.html', results=results, cities=searched_cities, c_u=city_users,thera_id=therapist_ids)
