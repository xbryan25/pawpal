from flask import request, jsonify
from app.models import Pet, PetImage, Shelter
from app import db
from datetime import datetime
import uuid
import cloudinary.uploader

def get_pet_list_controller():
    try:
        pets = db.session.query(Pet.pet_id, Pet.name, Pet.status, Pet.shelter_id).all()

        print(pets)

        pets_list = [{'petId': str(uuid.UUID(bytes=pet_id)), 
                      'name': name, 
                      'status': status.value,
                      'shelterId': str(uuid.UUID(bytes=shelter_id))} 
                      for pet_id, name, status, shelter_id in pets]
        
        for pet in pets_list:
            pet_first_image_url = db.session.query(PetImage.image_url).filter(uuid.UUID(pet['petId']).bytes == PetImage.pet_id).first()
            pet_shelter = db.session.query(Shelter.name).filter(uuid.UUID(pet['shelterId']).bytes == Shelter.shelter_id).first()

            pet.update({'petFirstImageUrl': pet_first_image_url[0]})
            pet.update({'petShelter': pet_shelter[0]})

            del pet["shelterId"]

        return jsonify(pets_list), 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def pet_registration_controller():
    pet_data = request.form
    pet_images = request.files

    try:
        pet_id = uuid.uuid4().bytes

        new_pet = Pet(
            pet_id=pet_id,
            name=pet_data['name'],
            birth_date=datetime.strptime(pet_data["birthDate"], "%Y-%m-%d").date(),
            sex=pet_data["sex"].lower(),
            status=pet_data["status"],
            description=pet_data["description"],
            breed_id=uuid.UUID(pet_data["breedId"]).bytes,
            species_id=uuid.UUID(pet_data["speciesId"]).bytes,
            shelter_id=uuid.UUID(pet_data["shelterId"]).bytes
        )

        db.session.add(new_pet)

        # This generates the pet_id and inserts it into the DB without committing
        db.session.flush()

        files = pet_images.getlist('petPhotos')  # Get all uploaded files

        for index, file in enumerate(files):
            result = cloudinary.uploader.upload(
                file,
                public_id=f"{str(uuid.UUID(bytes=pet_id))}-[{index + 1}]"
            )   

            pet_image = PetImage(
                image_url=result['secure_url'],
                uploaded_at=datetime.now(),
                sort_order=index+1,
                pet_id=pet_id
            )

            db.session.add(pet_image)

        db.session.commit()

        return jsonify({"message": "Pet registered successfully."}), 201

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
