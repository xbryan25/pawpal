from flask import Blueprint
from app.controllers import SpeciesController

species_bp = Blueprint("species_bp", __name__)


@species_bp.route("/list", methods=["GET"])
def get_species_list():
    return SpeciesController.get_species_list_controller()
