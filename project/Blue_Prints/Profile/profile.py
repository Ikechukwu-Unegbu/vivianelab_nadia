from flask import Blueprint, render_template
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User

profile = Blueprint('profile', __name__)

@profile.route('/dashboard/my/')
def myprofile():
   return "we are here"