from flask import Blueprint
from app.controllers import PetController

pet_bp = Blueprint("pet_bp", __name__)


@pet_bp.route("/register-pet", methods=["POST"])
def registration():
    return PetController.pet_registration_controller()

@pet_bp.route("/edit-pet", methods=["POST"])
def edit_pet():
    return PetController.pet_edit_controller()

@pet_bp.route("/get-details", methods=["GET"])
def get_pet_details():
    return PetController.get_pet_details_controller()

@pet_bp.route("/get-adoption-status", methods=["GET"])
def get_adoption_status():
    return PetController.get_adoption_status_controller()

@pet_bp.route("/list", methods=["GET"])
def get_pet_list():
    return PetController.get_pet_list_controller()

@pet_bp.route("/adopt-pet", methods=["POST"])
def adopt_pet():
    return PetController.pet_adoption_controller()

@pet_bp.route("/cancel-pet-adoption", methods=["POST"])
def cancel_pet_adoption():
    return PetController.cancel_pet_adoption_controller()