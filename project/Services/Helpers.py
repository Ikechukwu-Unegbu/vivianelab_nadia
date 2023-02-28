from ..models.Admin import Admin
from ..models.User import User


def get_user_type(user):
    if isinstance(user, User):
        return 'user'
    elif isinstance(user, Admin):
        return 'admin'
    else:
        return 'unknown'

# def get_user_withID_by_type(user):
#     if isinstance(user, User):
#         return 
#     elif isinstance(user, Therapist):
#         return 'therapist'
#     elif isinstance(user, Admin):
#         return 'admin'
#     else:
#         return 'unknown'
