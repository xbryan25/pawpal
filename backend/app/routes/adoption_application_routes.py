from flask import Blueprint, jsonify, request
from app.controllers import get_num_of_pet_adoption_applications_controller

adoption_application_bp = Blueprint("adoption_application_bp", __name__)


@adoption_application_bp.route("/get-pet-adoption-applications_num", methods=["GET"])
def get_num_of_pet_adoption_applications():
    return get_num_of_pet_adoption_applications_controller()
