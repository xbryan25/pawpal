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
        
    @staticmethod
    def get_application_details_controller():

        aa_id_str = request.args.get("applicationId")

        if not aa_id_str:
            return jsonify({"error": "applicationId is required"}), 400

        try:

            aa_id = uuid.UUID(aa_id_str).bytes

            adoption_application_details = AdoptionApplicationService.get_application_details(aa_id)

            return jsonify(adoption_application_details), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def approve_application_controller():
        data = request.json

        aa_id_str = data["applicationId"]

        if not aa_id_str:
            return jsonify({"error": "applicationId is required"}), 400

        try:

            aa_id = uuid.UUID(aa_id_str).bytes

            AdoptionApplicationService.approve_application(aa_id)

            return jsonify({"message": "Adoption application has been approved."}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def reject_application_controller():
        data = request.json

        aa_id_str = data["applicationId"]

        if not aa_id_str:
            return jsonify({"error": "applicationId is required"}), 400

        try:

            aa_id = uuid.UUID(aa_id_str).bytes

            AdoptionApplicationService.reject_application(aa_id)

            return jsonify({"message": "Adoption application has been rejected."}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500


    @staticmethod
    def get_application_reports_controller():

        selected_range = request.args.get("selectedRange")
        first_value = request.args.get("firstValue")
        shelter_id_str = request.args.get("shelterId")

        try:
            
            shelter_id = uuid.UUID(shelter_id_str).bytes if shelter_id_str else None

            applications_frequency = AdoptionApplicationService.get_applications_frequency(selected_range, first_value, shelter_id)

            applications_status_frequency = AdoptionApplicationService.get_application_status_frequency(shelter_id)

            # types_of_adopted_pets_frequency = AdoptionApplicationService.get_types_of_adopted_pets_frequency(shelter_id)

            print(applications_status_frequency)


            return jsonify({'applicationsFrequency': applications_frequency, 'applicationStatusFrequency': applications_status_frequency}), 200

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500
        