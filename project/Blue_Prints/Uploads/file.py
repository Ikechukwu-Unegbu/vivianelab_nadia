from flask import Blueprint, render_template
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User

file_upload = Blueprint('profile', __name__, template_folder='templates', static_folder="static", static_url_path='/profile/static')

@file_upload.route('/dp/upload/')
def profilepic_upload():
    # make sure that given id is same as auth user id

    therapist = Therapist.query.filter_by(id=current_user.id).first()
    # get type instance of logged in user
    #  fetch user deatails from the right table

    return render_template('/profile/profile.html', therapist=therapist)

@file_upload.route('/govid/upload')
def govupload():
    return "upload"