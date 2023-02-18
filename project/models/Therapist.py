import random
from flask_login import UserMixin
from .. import db 
from enum import Enum
from sqlalchemy import Column
from .BaseModel import BaseModel
class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'


class Therapist(BaseModel,UserMixin, db.Model):
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
    bio = db.Column(db.Text(), nullable=True)
    tagline = db.Column(db.Text(), nullable=True)


    @classmethod
    def get_all(cls):
        return cls.query.all()



    @classmethod
    def get_random_therapists(cls, num_therapists=5):
        # get the total number of therapists in the table
        total_therapists = cls.query.count()

        # get five random therapist objects from the table
        random_therapists = []
        for _ in range(num_therapists):
            # generate a random index for the therapist to retrieve
            rand_index = random.randint(0, total_therapists - 1)
            # retrieve the therapist at the generated index
            therapist = cls.query.offset(rand_index).first()
            # add the therapist to the list of random therapists
            random_therapists.append(therapist)

        return random_therapists

    



