from flask import request, jsonify

from app.models.shelter import Shelter
from app import db
import uuid


def get_shelter_list_controller():
    try:
        shelters = db.session.query(Shelter.shelter_id, Shelter.name).all()

        shelters_list = [{'shelter_id': str(uuid.UUID(bytes=shelter_id)), 'name': name} for shelter_id, name in shelters]

        return jsonify(shelters_list), 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

