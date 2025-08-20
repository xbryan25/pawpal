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

        user_id_str = request.args.get("userId")

        if not user_id_str:
            return jsonify({"error": "userId is required"}), 400

        try:
            userId = uuid.UUID(user_id_str).bytes

            adopterApplications = AdoptionApplicationService.get_adopter_applications(userId)

            return jsonify({"adopterApplications": adopterApplications}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_shelter_applications_controller():

        shelter_id_str = request.args.get("shelterId")

        if not shelter_id_str:
            return jsonify({"error": "shelterId is required"}), 400

        try:

            shelter_id = uuid.UUID(shelter_id_str).bytes

            shelterApplications = AdoptionApplicationService.get_shelter_applications(shelter_id)

            return jsonify({"shelterApplications": shelterApplications}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500
