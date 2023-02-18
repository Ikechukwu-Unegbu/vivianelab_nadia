# from flask_login import UserMixin
from flask import current_app
from .. import db 
from enum import Enum
# db = current_app.db


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    therapist_id = db.Column(db.Integer)
    employer = db.Column(db.String(200))
    jobrole = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text(), nullable=True)  
    starting_month = db.Column(db.Integer(), nullable=True)  
    starting_year = db.Column(db.Integer(), nullable=True)  
    ending_month = db.Column(db.Integer(), nullable=True)  
    ending_year = db.Column(db.Integer(), nullable=True)  