from flask import Blueprint, render_template
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User

profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/dashboard/my/')
def myprofile():
    # make sure that given id is same as auth user id
    # get type instance of logged in user
    #  fetch user deatails from the right table

   return render_template('profile.html')
