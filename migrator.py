from flask import current_app
from project.models.Appointment import add_created_at_column_to_appointment_model

add_created_at_column_to_appointment_model()

with current_app.app_context():
    add_created_at_column_to_appointment_model()
    current_app.run()
    