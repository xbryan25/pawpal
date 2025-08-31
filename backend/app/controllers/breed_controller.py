from flask import request, jsonify

from app.extensions import db
from app.services import BreedService


class BreedController:

    @staticmethod
    def get_breed_list_controller():
        species_name = request.args.get("species_name")

        try:
            breeds_list = BreedService.get_breeds_list(species_name)
            return jsonify(breeds_list), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_all_breed_details_controller():

        try:
            all_breed_details = BreedService.get_all_breed_details()
            return jsonify({'allBreedDetails': all_breed_details}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
