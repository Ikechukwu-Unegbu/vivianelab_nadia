from flask import Blueprint, render_template
from ... import db
from flask_login import login_required, current_user
from ...models.Therapist import Therapist
from ...Services.Helpers import get_user_type
# from .Services.Helpers import get_user_type
# from .models.Therapist import Therapist
from ...models.User import User

settings = Blueprint('settings', __name__, template_folder='templates', static_folder="static", static_url_path='/Settings/static')


@settings.route('/settings')
def govupload():
    return "settings"

@settings.route('/notification/settings')
def notification_settings():
    return render_template('notification_settings.html')

@settings.route('/visibility/settings')
def visibility_settings():
    return render_template('notification_settings.html')

@settings.route('/security/settings')
def security_settings():
    return render_template('security_settings.html')


@settings.route('/payment/settings')
def payment_settings():
    return render_template('payment_settings.html')



