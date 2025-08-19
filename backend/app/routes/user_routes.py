from flask import Blueprint
from app.controllers import UserController

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/login", methods=["POST"])
def login():
    return UserController.user_login_controller()


@user_bp.route("/signup", methods=["POST"])
def new_user_signup():
    return UserController.user_signup_controller()
