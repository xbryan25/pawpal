from flask import Blueprint, jsonify, request
from app.controllers import get_breed_list_controller

breed_bp = Blueprint("breed_bp", __name__)


@breed_bp.route("/list", methods=["GET"])
def get_breed_list():
    return get_breed_list_controller()
