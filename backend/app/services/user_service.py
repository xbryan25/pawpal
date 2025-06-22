from app.models.user import User
from werkzeug.security import check_password_hash


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and User.check_password(password):
        return user
    return None
