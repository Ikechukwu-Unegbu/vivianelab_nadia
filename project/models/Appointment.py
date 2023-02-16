from flask_login import UserMixin
from .. import db 
from enum import Enum

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    therapist_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    location_id = db.Column(db.Integer)
    address = db.Column(db.Text)
    description = db.Column(db.Text, nullable=True)
    arrive_user = db.Column(db.DateTime, nullable=True)
    arrive_therapist = db.Column(db.DateTime, nullable=True)
    done_user = db.Column(db.DateTime, nullable=True)
    done_therapist = db.Column(db.DateTime, nullable=True)
    cancel =  db.Column(db.Integer,nullable=True, default=0)
    cancel_by =  db.Column(db.Integer,nullable=True)
