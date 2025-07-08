from flask import Blueprint, jsonify, request
from app.controllers import get_shelter_list_controller

shelter_bp = Blueprint("shelter_bp", __name__)


@shelter_bp.route("/list", methods=["GET"])
def get_shelter_list():
    return get_shelter_list_controller()
