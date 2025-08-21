from flask import Blueprint
from app.controllers import AdoptionApplicationController 

adoption_application_bp = Blueprint("adoption_application_bp", __name__)


@adoption_application_bp.route("/get-pet-adoption-applications_num", methods=["GET"])
def get_num_of_pet_adoption_applications():
    return AdoptionApplicationController.get_num_of_pet_adoption_applications_controller()

@adoption_application_bp.route("/get-adopter-applications", methods=["GET"])
def get_adopter_applications():
    return AdoptionApplicationController.get_adopter_applications_controller()

@adoption_application_bp.route("/get-shelter-applications", methods=["GET"])
def get_shelter_applications():
    return AdoptionApplicationController.get_shelter_applications_controller()

@adoption_application_bp.route("/get-application-details", methods=["GET"])
def get_application_details():
    return AdoptionApplicationController.get_application_details_controller()
