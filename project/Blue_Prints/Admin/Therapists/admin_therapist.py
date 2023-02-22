from flask import Blueprint, render_template, request, redirect, flash,jsonify
from ....models.Therapist import Therapist
from ....models.User import User
from ....import db
from ....models.Locations.Country import Country
from ....models.Locations.State import State
from ....models.Locations.City import City
from flask_login import login_required, current_user


admin_therapist = Blueprint('admin_location', __name__, template_folder='templates', static_folder="static", static_url_path='/Blue_Prints/Admin/General/static')
