from flask import Blueprint, jsonify, request
from app.controllers import pet_registration_controller, get_pet_list_controller

pet_bp = Blueprint("pet_bp", __name__)


@pet_bp.route("/register-pet", methods=["POST"])
def registration():
    return pet_registration_controller()

@pet_bp.route("/list", methods=["GET"])
def get_shelter_list():
    return get_pet_list_controller()