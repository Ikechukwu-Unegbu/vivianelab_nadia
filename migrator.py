from project.models.Therapist import Therapist
from flask_migrate import Migrate
from project import db
from project import create_app

app = create_app()

migrate = Migrate(app, db)

with app.app_context():
    result = Therapist.add_column()


print(result)