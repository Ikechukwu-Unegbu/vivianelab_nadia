from project import create_app, db
from project.models.User import User

from project.models.Admin import Admin
from project.models.Appointment import Appointment
from project.models.Locations.City import City
# from flask import current_app
from project.models.Education import Education
from project.models.Locations.Country import Country
from project.models.Locations.State import State
from project.models.Locations.City import City
from project.models.Locations.UserCity import UserCity
from project.models.Notification import Notification

app = create_app()
# Appointment.add_created_at_column_to_appointment_model()
with app.app_context():
    db.create_all()

