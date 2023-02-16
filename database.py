from project import create_app, db
from project.models.User import User
from project.models.Therapist import Therapist
from project.models.Admin import Admin
from project.models.Appointment import Appointment
from project.models.City import City


app = create_app()

with app.app_context():
    db.create_all()
