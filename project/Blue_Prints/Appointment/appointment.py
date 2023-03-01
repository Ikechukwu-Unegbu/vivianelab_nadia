from flask import Blueprint, render_template, request, redirect, flash, url_for
from datetime import datetime
from ... import db
from flask_login import login_required, current_user
# from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
from ...models.Notification import Notification
from ...models.User import User
from ...Services import Helpers 
from werkzeug.security import generate_password_hash, check_password_hash
from ...models.Appointment import Appointment
# from ...models.Appointment import add_created_at_column_to_appointment_model


appointment = Blueprint('appointment', __name__, template_folder='templates', static_folder="static", static_url_path='/Appointment/static')

@appointment.route('/medic/appointments')
def medic_appointments():
    # Appointment.add_created_at_column_to_appointment_model
    return render_template('/medic/appointments.html')

@appointment.route('/medic/appointment/<string:username>')
def medic_single_appointment():
    return render_template('/medic/appointments.html')

@appointment.route('/appoint', methods=["POST"])
def book_appointment():
    therapist_id = request.form.get('therapist_id')
    city = request.form.get('city')
    address = request.form.get('address')
    description = request.form.get('description')
    session_date = request.form.get('session_date')
    arrive_user_dt = datetime.strptime(session_date, '%Y-%m-%d')

    appointment = Appointment(therapist_id=therapist_id,user_id=current_user.id, location_id=city, address=address, description=description,session_date=arrive_user_dt )

    # add the appointment to the database and commit the transaction
    db.session.add(appointment)
    db.session.commit()

    notification = Notification(user_id=therapist_id,message="You have new booking.",created_at=datetime.now(),is_read=False)
    db.session.add(notification)
    db.session.commit()
    return redirect(url_for('main.dashboard'))