from flask import Blueprint, jsonify, request
from app.controllers import pet_registration_controller, pet_edit_controller, get_pet_list_controller, get_pet_details_controller, pet_adoption_controller

pet_bp = Blueprint("pet_bp", __name__)


@pet_bp.route("/register-pet", methods=["POST"])
def registration():
    return pet_registration_controller()

@pet_bp.route("/edit-pet", methods=["POST"])
def edit_pet():
    return pet_edit_controller()

@pet_bp.route("/get-details", methods=["GET"])
def get_pet_details():
    return get_pet_details_controller()

@pet_bp.route("/list", methods=["GET"])
def get_pet_list():
    return get_pet_list_controller()

@pet_bp.route("/adopt-pet", methods=["POST"])
def adopt_pet():
    return pet_adoption_controller()