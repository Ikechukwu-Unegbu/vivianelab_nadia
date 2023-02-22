from project import create_app, db
# from project.models.User import User
# from project.models.Therapist import Therapist
# from project.models.Admin import Admin
# from project.models.Appointment import Appointment
from project.models.Locations.City import City
from flask import current_app
# from project.models.Education import Education
from project.models.Locations.Country import Country
from project.models.Locations.State import State


app = create_app()

with app.app_context():
    db.create_all()
