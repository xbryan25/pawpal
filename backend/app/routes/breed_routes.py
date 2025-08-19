from flask import Blueprint
from app.controllers import BreedController

breed_bp = Blueprint("breed_bp", __name__)


@breed_bp.route("/list", methods=["GET"])
def get_breed_list():
    return BreedController.get_breed_list_controller()
