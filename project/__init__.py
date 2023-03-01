from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user
# init SQLAlchemy so we can use it later in our models
from flask_migrate import Migrate



# migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['AVATAR_FOLDER'] = '/static/uploads/avatar'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    # migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from .models.User import User

     # @login_manager.user_loader
    # def load_user(user_id):
    #     # since the user_id is just the primary key of our user table, use it in the query for the user
    #     return User.query.get(int(user_id))

  
    @login_manager.user_loader
    def load_user(user_id):
        # Try to find the user in the User model
        user = User.query.get(int(user_id))
        if user is not None:
            return user
        # If still not found, return None
        return None


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # # profile blue prints
    from .Blue_Prints.Profile.profile import profile as profile_bluepring
    app.register_blueprint(profile_bluepring)

    from .Blue_Prints.Uploads.file import file_upload as fileupload_blueprint
    app.register_blueprint(fileupload_blueprint)

    from .Blue_Prints.Settings.settings import settings as settings_blueprint
    app.register_blueprint(settings_blueprint)
    


    from .Blue_Prints.Admin.General.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .Blue_Prints.Admin.Location.admin_location import admin_location as admin_location_blueprint
    app.register_blueprint(admin_location_blueprint)


    return app
