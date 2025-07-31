from flask import request, jsonify
from app.models.pet import Pet
from app.models.shelter import Shelter
from app import db
from datetime import datetime
import uuid


def pet_registration_controller():
    data = request.form
    files = request.files

    print(data)
    print(files)

    return jsonify({"message": "Pet created successfully"}), 201

    # try:
    #     new_pet = Pet(
    #         name=data["name"],
    #         birth_date=datetime.strptime(data["birthDate"], "%Y-%m-%d").date(),
    #         sex=data["sex"],
    #         status="available",
    #         description=data["description"],
    #         breed_id=data["breedId"],
    #         species_id=data["speciesId"],
    #         shelter_id=data["shelterId"]
    #     )

    #     db.session.add(new_pet)
    #     db.session.commit()

    #     return jsonify({"message": "Pet registered successfully"}), 201

    # except Exception as e:
    #     print(e)
    #     db.session.rollback()
    #     return jsonify({"error": str(e)}), 500
