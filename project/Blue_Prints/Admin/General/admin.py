from flask import Blueprint, render_template, request, redirect, flash
from ... import db
from ....models.Therapist import Therapist
from ....models.User import User
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


admin = Blueprint('admin', __name__, template_folder='templates', static_folder="static", static_url_path='/Admin/General/static')

@admin.route('admin/home')
def medic_appointments():
    return render_template('/medic/appointments.html')

@admin.route('/admin/home')
def admin_home():
    therapists = Therapist.query.all()
    users = User.query.all()
    return render_template('admin/home.html', therapists=therapists, users=users)