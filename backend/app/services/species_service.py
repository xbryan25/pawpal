from app.models import Species
from app.extensions import db

import uuid


class SpeciesService:

    @staticmethod
    def get_species_list():
        species = db.session.query(Species.species_id, Species.species_name).all()

        species_list = [{'species_id': str(uuid.UUID(bytes=shelter_id)), 'species_name': species_name} for shelter_id, species_name in species]

        return species_list
    