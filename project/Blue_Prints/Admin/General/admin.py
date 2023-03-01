from flask import Blueprint, render_template, request, redirect, flash
from ....models.User import User
from ....models.Locations.Country import Country
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ....import db

admin = Blueprint('admin', __name__, template_folder='templates', static_folder="static", static_url_path='/Blue_Prints/Admin/General/static')

@admin.route('/admin/home')
def admin_home():
    """
        This endpoint renders admin homepage.
    """ 
    
    countries = Country.query.all()
    users = User.query.filter(User.access.in_(['user', 'USER'])).all()
    therapists = User.query.filter(User.access.in_(['therapist', 'THERAPIST'])).all()
    return render_template('admin/home/home.html', therapists=therapists, users=users, countries=countries)

@admin.route('/admin/locations')
def admin_locations():
    countries = Country.query.all()
    return render_template('admin/locations/index.html', countries=countries)


@admin.route('/admin/therapists') 
def admin_therapists(): 
    countries = Country.query.all()
    return render_template('admin/therapists/admin_therapists.html', countries=countries)
