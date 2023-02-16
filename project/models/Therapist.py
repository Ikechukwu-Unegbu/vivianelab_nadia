from flask_login import UserMixin
from .. import db 
from enum import Enum

class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'


class Therapist(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(120))
    fullname = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    gender = db.Column(db.Enum(GenderEnum), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    city_id = db.Column(db.Integer, nullable=True)
    avatar = db.Column(db.String(200), nullable=True)
    govcard = db.Column(db.String(200), nullable=True)
    verified = db.Column(db.Integer(),nullable=True, default=0)
    addrss = db.Column(db.Text(), nullable=True)
    blocked = db.Column(db.Integer,nullable=True, default=0)        


    @classmethod
    def get_all(cls):
        return cls.query.all()