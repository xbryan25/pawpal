from flask import Blueprint
from app.controllers import ShelterController

shelter_bp = Blueprint("shelter_bp", __name__)


@shelter_bp.route("/list", methods=["GET"])
def get_shelter_list():
    return ShelterController.get_shelter_list_controller()
