from app.models import Breed, Species, Pet
from app.extensions import db

import uuid


class BreedService:

    @staticmethod
    def get_breeds_list(species_name):
        species_id = db.session.query(Species.species_id).filter(Species.species_name == species_name).scalar()

        breeds = db.session.query(Breed.breed_id, Breed.breed_name).filter(Breed.species_id == species_id).all()

        breeds_list = [{'breed_id': str(uuid.UUID(bytes=breed_id)), 'breed_name': breed_name} for breed_id, breed_name in breeds]

        return breeds_list
    
    
    @staticmethod
    def get_all_breed_details():
        
        all_breed_details = []

        breeds = db.session.query(Breed.breed_id, Breed.species_id, Breed.breed_name).all()

        for breed in breeds:
            species_name = db.session.query(Species.species_name).filter(Species.species_id == breed.species_id).scalar()

            num_of_registered_pets = db.session.query(Pet).filter(Pet.breed_id == breed.breed_id).count()

            all_breed_details.append({'breedName': breed.breed_name, 
                                      'speciesName': species_name,
                                      'numOfRegisteredPets': num_of_registered_pets})

        return all_breed_details