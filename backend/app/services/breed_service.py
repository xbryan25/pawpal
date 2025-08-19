from app.models import Breed, Species
from app.extensions import db

import uuid


class BreedService:

    @staticmethod
    def get_breeds_list(species_name):
        species_id = db.session.query(Species.species_id).filter(Species.species_name == species_name).scalar()

        breeds = db.session.query(Breed.breed_id, Breed.breed_name).filter(Breed.species_id == species_id).all()

        breeds_list = [{'breed_id': str(uuid.UUID(bytes=breed_id)), 'breed_name': breed_name} for breed_id, breed_name in breeds]

        return breeds_list