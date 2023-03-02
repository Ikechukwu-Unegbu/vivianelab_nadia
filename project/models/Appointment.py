from flask import current_app
from datetime import datetime
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    session_date = db.Column(db.DateTime, nullable=True)
    # user = db.relationship('User', backref='appointments')
    
    # @classmethod
    # def add_created_at_column_to_appointment_model():
    #     db.session.rollback()

    #     # Check if the column already exists
    #     if hasattr(Appointment, 'created_at'):
    #         return

    #     # Add the column
    #     db.session.execute('ALTER TABLE appointment ADD COLUMN created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW();')
    #     db.session.commit()

    #     # Reflect the changes in the model
    #     db.session.expire_all()
    #     db.session.refresh(Appointment)
    #     print("added")
    #     return

    
