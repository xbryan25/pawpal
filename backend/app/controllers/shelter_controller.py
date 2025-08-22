from flask import jsonify

from app.services import ShelterService
from app.extensions import db


class ShelterController:
    
    @staticmethod
    def get_shelter_list_controller():
        try:
            shelters_list = ShelterService.get_shelters_list()

            return jsonify(shelters_list), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

