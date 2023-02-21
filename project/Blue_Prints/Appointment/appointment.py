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


appointment = Blueprint('appointment', __name__, template_folder='templates', static_folder="static", static_url_path='/Appointment/static')

@appointment.route('/medic/appointments')
def medic_appointments():
    return render_template('/medic/appointments.html')

@appointment.route('/medic/appointment/<string:username>')
def medic_single_appointment():
    return render_template('/medic/appointments.html')
