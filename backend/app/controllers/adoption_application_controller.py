from flask import request, jsonify
import uuid

from app.services import get_num_of_adoption_applications, getAdopterApplications


def get_num_of_pet_adoption_applications_controller():
    try:

        pet_id = uuid.UUID(request.args.get("petId")).bytes

        num_of_adoption_applications = get_num_of_adoption_applications(pet_id)

        return jsonify({"count": num_of_adoption_applications}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


def get_adopter_applications_controller():
    try:

        userId = uuid.UUID(request.args.get("userId")).bytes

        adopterApplications = getAdopterApplications(userId)

        return jsonify({"adopterApplications": adopterApplications}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
