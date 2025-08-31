from app.models import Species, Pet, Breed
from app.extensions import db

import uuid


class SpeciesService:

    @staticmethod
    def get_species_list():
        species = db.session.query(Species.species_id, Species.species_name).all()

        species_list = [{'species_id': str(uuid.UUID(bytes=shelter_id)), 'species_name': species_name} for shelter_id, species_name in species]

        return species_list
    
    @staticmethod
    def get_all_species_details():
        
        all_species_details = []

        species = db.session.query(Species.species_id, Species.species_name).all()

        for singular_species in species:
            num_of_registered_pets = (db.session.query(Pet)
                                      .join(Breed, Pet.breed_id == Breed.breed_id)
                                      .filter(Breed.species_id == singular_species.species_id)
                                      .count())
            
            print(num_of_registered_pets)

            all_species_details.append({'speciesName': singular_species.species_name,
                                      'numOfRegisteredPets': num_of_registered_pets})

        return all_species_details
    