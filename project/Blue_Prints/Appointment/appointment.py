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
    page = request.args.get('page', 1, type=int)
    appointments = Appointment.query.join(User, Appointment.user_id == User.id). \
                  filter(Appointment.therapist_id == current_user.id). \
                  paginate(page=page, per_page=10)
    
    # Add user object to each appointment
    for appointment in appointments.items:
        appointment.user = User.query.get(appointment.user_id)


    return render_template('/medic/appointments.html', appointments=appointments)


@appointment.route('/user/appointments')
def patient_appointments():
    page = request.args.get('page', 1, type=int)
    appointments = Appointment.query.join(User, Appointment.user_id == User.id). \
                  filter(Appointment.user_id == current_user.id). \
                  paginate(page=page, per_page=10)
    
    # Add user object to each appointment
    for appointment in appointments.items:
        appointment.therapist = User.query.get(appointment.therapist_id)

    return render_template('/patient/user_appointments.html', appointments=appointments)



@appointment.route('/appointment/<string:action>/<int:id>')
def appointment_action_toggle(action,id):
    appointment = Appointment.query.get(id)

    if action == "accept": 
        # accept but since cancel is true by default.... lets notify the user of acceptance.
        # Create a new notification object
        notification = Notification(
            user_id=appointment.user_id,  # set the user_id
            message="Medic accepted your appointment",  # set the message
            created_at=datetime.utcnow(),  # set the current timestamp
            is_read=False  # set is_read to False by default
        )
        # Add the notification object to the session and commit
        db.session.add(notification)
        db.session.commit()
        flash_message = "You have accepted this appointment."
    if action == "cancel":
        appointment.cancel_by = current_user.id
        db.session.add(appointment)
        db.session.commit()
        notification = Notification(
            user_id=appointment.user_id,  # set the user_id
            message="Medic declined your appointment",  # set the message
            created_at=datetime.utcnow(),  # set the current timestamp
            is_read=False  # set is_read to False by default
        )
        # Add the notification object to the session and commit
        db.session.add(notification)
        db.session.commit()
        flash_message = "You have successfully declined this appointment"

    flash(flash_message)
    return redirect(request.referrer)


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

