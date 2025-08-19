from flask import request, jsonify
import uuid

from app.services import AdoptionApplicationService


class AdoptionApplicationController:

    @staticmethod
    def get_num_of_pet_adoption_applications_controller():
        
        pet_id_str = request.args.get("petId")

        if not pet_id_str:
            return jsonify({"error": "petId is required"}), 400

        try:
            pet_id = uuid.UUID(pet_id_str).bytes

            num_of_adoption_applications = AdoptionApplicationService.get_num_of_adoption_applications(pet_id)

            return jsonify({"count": num_of_adoption_applications}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_adopter_applications_controller():

        user_id_str = request.args.get("petId")

        if not user_id_str:
            return jsonify({"error": "petId is required"}), 400

        try:
            userId = uuid.UUID(user_id_str).bytes

            adopterApplications = AdoptionApplicationService.getAdopterApplications(userId)

            return jsonify({"adopterApplications": adopterApplications}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500
