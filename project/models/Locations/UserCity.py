# from flask_login import UserMixin
from ... import db 
from enum import Enum
from datetime import datetime



class UserCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    city_id = db.Column(db.String(200))
    user_model = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # postal = db.Column(db.String(20), nullable=True)
