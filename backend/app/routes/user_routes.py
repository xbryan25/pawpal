from flask import Blueprint, jsonify, request
from app.controllers.user_controller import user_login_controller, user_signup_controller

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/login", methods=["POST"])
def login():
    return user_login_controller()


@user_bp.route("/signup", methods=["POST"])
def new_user_signup():
    return user_signup_controller()
