from flask import Blueprint, render_template, request, redirect, flash,jsonify
from ....models.Therapist import Therapist
from ....models.User import User
from ....import db
from ....models.Locations.Country import Country
from ....models.Locations.State import State
from ....models.Locations.City import City
from flask_login import login_required, current_user


admin_location = Blueprint('admin_location', __name__, template_folder='templates', static_folder="static", static_url_path='/Blue_Prints/Admin/General/static')

@admin_location.route('/new/country', methods=["POST"])
def save_country():
    name = request.form.get('name')
    capital = request.form.get('capital')

    country = Country(name=name, capital=capital)
    db.session.add(country)
    db.session.commit()
    flash('New country added to database')
    return redirect(request.referrer)


@admin_location.route('/new/state', methods=["POST"])
def save_state():
    name = request.form.get('name')
    capital = request.form.get('capital')
    country_id = request.form.get('country')

    country = State(country_id=country_id,name=name, capital=capital)
    db.session.add(country)
    db.session.commit()
    flash('New state added to database')
    return redirect(request.referrer)


@admin_location.route('/new/city', methods=["POST"])
def save_city():
    name = request.form.get('name')
    state_id = request.form.get('state')
    # country_id = request.form.get('country')

    city = City(state_id=state_id,name=name)
    db.session.add(city)
    db.session.commit()
    flash('New state added to database')
    return redirect(request.referrer)
    
    # return redirect(request.referrer)


@admin_location.route('/cities-by-state/<int:state_id>')
def get_cities_by_state(state_id):
    cities = City.query.filter_by(state_id=state_id).all()
    city_list = [{'id': c.id, 'name': c.name} for c in cities]
    return jsonify(city_list)

@admin_location.route('/states-by-country/<int:country_id>')
def get_states_by_country(country_id):
    states = State.query.filter_by(country_id=country_id).all()
    state_list = []
    for state in states:
        state_list.append({
            'id': state.id,
            'name': state.name,
            'capital':state.capital,
            'country_id': state.country_id
        })
    return jsonify(state_list)