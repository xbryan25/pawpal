from flask import Blueprint, jsonify, request
from app.controllers import get_species_list_controller

species_bp = Blueprint("species_bp", __name__)


@species_bp.route("/list", methods=["GET"])
def get_species_list():
    return get_species_list_controller()
