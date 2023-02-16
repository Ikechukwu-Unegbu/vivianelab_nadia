from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
from .Services.Helpers import get_user_type
from .models.Therapist import Therapist
from .models.User import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/dashboard')
@login_required
def dashboard():
    user_type = get_user_type(current_user)
    if user_type == 'user':
        return render_template('authenticated/user_dashboard.html')
    if user_type == 'therapist':
        return render_template('authenticated/therapist_dashboard.html')

@main.route('/admin/home')
def admin_home():
    therapists = User.query.all()
    return render_template('admin/home.html', therapists=therapists)