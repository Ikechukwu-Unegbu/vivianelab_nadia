from ..models.Admin import Admin
from ..models.User import User
from ..models.Therapist import Therapist

def get_user_type(user):
    if isinstance(user, User):
        return 'user'
    elif isinstance(user, Therapist):
        return 'therapist'
    elif isinstance(user, Admin):
        return 'admin'
    else:
        return 'unknown'
