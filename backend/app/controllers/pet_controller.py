from flask import request, jsonify
from app.models import Pet, PetImage, Shelter, Breed, Species
from app import db
from datetime import datetime
import uuid
import cloudinary.uploader
import json
from urllib.parse import urlparse
import os

def get_pet_list_controller():
    try:
        pets = db.session.query(Pet.pet_id, Pet.name, Pet.status, Pet.shelter_id).all()

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

def get_pet_details_controller():
    pet_id_str = request.args.get('petId')

    selected_pet = db.session.query(Pet).filter(Pet.pet_id == uuid.UUID(pet_id_str).bytes).first()

    selected_pet_breed = db.session.query(Breed.breed_name).filter(selected_pet.breed_id == Breed.breed_id).first()[0]
    selected_pet_species = db.session.query(Species.species_name).filter(selected_pet.species_id == Species.species_id).first()[0]
    selected_pet_shelter = db.session.query(Shelter.name).filter(selected_pet.shelter_id == Shelter.shelter_id).first()[0]

    selected_pet_image_urls_tuples = db.session.query(PetImage.image_url, PetImage.sort_order).filter(uuid.UUID(pet_id_str).bytes == PetImage.pet_id).order_by(PetImage.sort_order).all()

    selected_pet_image_urls = [{'image_url': image_url, 
                                'sort_order': sort_order} 
                                for image_url, sort_order in selected_pet_image_urls_tuples]

    selected_pet_dict = {'petId': pet_id_str, 
                         'name': selected_pet.name, 
                         'birthDate': selected_pet.birth_date.strftime("%B %d, %Y"), 
                         'sex': selected_pet.sex.value, 
                         'status': selected_pet.status.value,
                         'description': selected_pet.description,
                         'breed': selected_pet_breed,
                         'species': selected_pet_species,
                         'shelter': selected_pet_shelter,
                         'petImages': selected_pet_image_urls}

    return jsonify(selected_pet_dict), 201

def pet_registration_controller():
    pet_data = request.form
    pet_images = request.files

    try:

        print(pet_data)
        print(pet_images)

        files = []

        for value in pet_images.values():
            files.append(value)

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

        for index, file in enumerate(files):
            # Create a new uuid just for the image link

            result = cloudinary.uploader.upload(
                file,
                public_id=f"{str(uuid.uuid4())}"
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

def pet_edit_controller():
    pet_data = request.form
    pet_images = request.files

    try:
        pet_id_str = pet_data["petId"]

        current_pet = Pet.query.filter_by(pet_id=uuid.UUID(pet_id_str).bytes).first()

        # First part, edit text data
        current_pet.name = pet_data["name"]
        current_pet.birth_date = datetime.strptime(pet_data["birthDate"], "%Y-%m-%d").date()
        current_pet.sex = pet_data["sex"].lower()
        current_pet.status = pet_data["status"]
        current_pet.description = pet_data["description"]
        current_pet.breed_id = uuid.UUID(pet_data["breedId"]).bytes
        current_pet.species_id = uuid.UUID(pet_data["speciesId"]).bytes
        current_pet.shelter_id = uuid.UUID(pet_data["shelterId"]).bytes

        # Second part, edit images
        existing_pet_images = PetImage.query.filter_by(pet_id=uuid.UUID(pet_id_str).bytes).all()

        request_image_meta = {}
        request_image_urls_meta = {}
        request_image_urls = []

        for i in range(1, 6):
            image_meta_str = request.form.get(f"petImagesMeta-{i}")

            if image_meta_str:
                image_meta = json.loads(image_meta_str)

                request_image_meta.update({f"petImagesMeta-{i}": image_meta})

                if image_meta["mode"] == 'edit':

                    image_meta.pop("mode")
                    
                    request_image_urls_meta.update({f"petImagesMeta-{i}": image_meta})
                    request_image_urls.append(image_meta["imageUrl"])
                
                
        for existing_pet_image in existing_pet_images:
            if existing_pet_image.image_url not in request_image_urls:
                print(f"image with sort order {existing_pet_image.sort_order} not in request_image_urls")

                try:
                    path = urlparse(existing_pet_image.image_url).path
                    public_id_with_version = path.split("/upload/")[1]
                    public_id_with_extension = os.path.splitext(public_id_with_version)[0]
                    public_id = "/".join(public_id_with_extension.split("/")[1:])
                except (IndexError, ValueError) as e:
                    print(f"Error parsing public_id: {e}")
                    continue  # Skip deletion if URL is invalid

                # Delete from Cloudinary first
                try:
                    cloudinary.uploader.destroy(public_id)
                except Exception as e:
                    print(f"Cloudinary deletion failed for {public_id}: {e}")
                    continue  # Skip DB deletion if Cloudinary failed

                # Delete from DB
                db.session.delete(existing_pet_image)

        
        for request_image_url_meta in request_image_urls_meta.values():
            if "imageUrl" in request_image_url_meta:
                for existing_pet_image in existing_pet_images:
                    if request_image_url_meta["imageUrl"] == existing_pet_image.image_url:

                        existing_pet_image.sort_order = request_image_url_meta["sortOrder"]

        for file_number_str, file in pet_images.items():
            file_number = int(file_number_str.replace('petImagesFile-', ''))

            result = cloudinary.uploader.upload(
                file,
                public_id=f"{str(uuid.uuid4())}"
            )   

            pet_image = PetImage(
                image_url=result['secure_url'],
                uploaded_at=datetime.now(),
                sort_order=file_number,
                pet_id=uuid.UUID(pet_id_str).bytes
            )

            db.session.add(pet_image)

        db.session.commit()

        return jsonify({"message": "Pet edited successfully."}), 201

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500