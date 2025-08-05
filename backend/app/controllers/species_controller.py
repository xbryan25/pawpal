from flask import request, jsonify

from app.models import Species
from app import db
import uuid


def get_species_list_controller():
    try:
        species = db.session.query(Species.species_id, Species.species_name).all()

        species_list = [{'species_id': str(uuid.UUID(bytes=shelter_id)), 'species_name': species_name} for shelter_id, species_name in species]

        return jsonify(species_list), 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

