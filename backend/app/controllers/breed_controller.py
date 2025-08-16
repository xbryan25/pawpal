from flask import request, jsonify

from app.models import Breed, Species
from app.extensions import db
import uuid


def get_breed_list_controller():
    try:
        species_name = request.args.get("species_name")

        species_id = db.session.query(Species.species_id).filter(Species.species_name == species_name).scalar()

        breeds = db.session.query(Breed.breed_id, Breed.breed_name).filter(Breed.species_id == species_id).all()

        breeds_list = [{'breed_id': str(uuid.UUID(bytes=breed_id)), 'breed_name': breed_name} for breed_id, breed_name in breeds]

        return jsonify(breeds_list), 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

