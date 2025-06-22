from flask import Blueprint, jsonify
from app.controllers.user_controller import login_controller

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/login", methods=["POST"])
def login():
    print("reach here?")
    return login_controller()


@user_bp.route("/login", methods=["GET"])
def login_get():
    print("reach here?")
    return jsonify({"message": "Test"}), 200
