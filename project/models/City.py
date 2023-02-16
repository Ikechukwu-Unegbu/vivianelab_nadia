# from flask_login import UserMixin
from .. import db 
from enum import Enum



class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    postal = db.Column(db.String(20), nullable=True)
