from flask import request, jsonify

from app.extensions import db
from app.services import PetService, AdoptionApplicationService

import uuid


class PetController:

    @staticmethod
    def get_pet_list_controller():
        try:
            pets_list = PetService.get_pet_list()
            return jsonify(pets_list), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_pet_details_controller():
        pet_id_str = request.args.get('petId')

        if not pet_id_str:
            return jsonify({"error": "petId is required"}), 400

        try: 
            pet_id = uuid.UUID(request.args.get("petId")).bytes

            pet_details = PetService.get_pet_details(pet_id)
            return jsonify(pet_details), 200

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def pet_registration_controller():
        pet_data = request.form
        pet_images = request.files

        if not pet_data:
            return jsonify({"error": "Pet data is required."}), 400
        elif not pet_images:
            return jsonify({"error": "Pet images are required."}), 400
        elif not pet_data and not pet_images:
            return jsonify({"error": "Pet data and images are required."}), 400

        try:
            PetService.register_pet(pet_data, pet_images)
            return jsonify({"message": "Pet registered successfully."}), 201

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def pet_edit_controller():
        pet_data = request.form
        pet_images = request.files

        if not pet_data:
            return jsonify({"error": "Pet data is required."}), 400
        elif not pet_images:
            return jsonify({"error": "Pet images are required."}), 400
        elif not pet_data and not pet_images:
            return jsonify({"error": "Pet data and images are required."}), 400

        try:
            PetService.edit_pet(pet_data, pet_images)

            return jsonify({"message": "Pet edited successfully."}), 201

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    
    @staticmethod
    def pet_adoption_controller():
        data = request.json

        user_id_str = data["userId"]
        pet_id_str = data["petId"]

        if not user_id_str:
            return jsonify({"error": "userId is required."}), 400
        elif not pet_id_str:
            return jsonify({"error": "petId is required."}), 400
        elif not user_id_str and not pet_id_str:
            return jsonify({"error": "userId and petId are required."}), 400

        try: 
            user_id = uuid.UUID(user_id_str).bytes
            pet_id = uuid.UUID(pet_id_str).bytes

            PetService.adopt_pet(user_id, pet_id)

            return jsonify({"message": "Adoption application was successfully made."}), 201 
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    
    @staticmethod
    def cancel_pet_adoption_controller():
        data = request.json

        user_id_str = data["userId"]
        pet_id_str = data["petId"]

        if not user_id_str:
            return jsonify({"error": "userId is required."}), 400
        elif not pet_id_str:
            return jsonify({"error": "petId is required."}), 400
        elif not user_id_str and not pet_id_str:
            return jsonify({"error": "userId and petId are required."}), 400

        try: 
            user_id = uuid.UUID(user_id_str).bytes
            pet_id = uuid.UUID(pet_id_str).bytes

            PetService.cancel_pet_adoption(user_id, pet_id)
            return jsonify({"message": "Adoption application was successfully cancelled."}), 201 
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_adoption_status_controller():

        pet_id_str = request.args.get('petId')
        user_id_str = request.args.get('userId')

        if not user_id_str:
            return jsonify({"error": "userId is required."}), 400
        elif not pet_id_str:
            return jsonify({"error": "petId is required."}), 400
        elif not user_id_str and not pet_id_str:
            return jsonify({"error": "userId and petId are required."}), 400
        
        try: 
            user_id = uuid.UUID(user_id_str).bytes
            pet_id = uuid.UUID(pet_id_str).bytes

            if AdoptionApplicationService.check_if_user_has_adoption_application(user_id, pet_id):
                return jsonify({"adoptionStatus": "adopted"}), 201 
            else:
                return jsonify({"adoptionStatus": "notAdopted"}), 201 

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
