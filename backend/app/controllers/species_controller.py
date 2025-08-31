from flask import request, jsonify

from app.services import SpeciesService
from app.extensions import db


class SpeciesController:

    @staticmethod
    def get_species_list_controller():
        try:
            species_list = SpeciesService.get_species_list()

            return jsonify(species_list), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_all_species_details_controller():

        try:
            all_species_details = SpeciesService.get_all_species_details()
            return jsonify({'allSpeciesDetails': all_species_details}), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
        