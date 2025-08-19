from app.models import Shelter
from app.extensions import db

import uuid


class ShelterService:

    @staticmethod
    def get_shelters_list():
        shelters = db.session.query(Shelter.shelter_id, Shelter.name).all()

        shelters_list = [{'shelter_id': str(uuid.UUID(bytes=shelter_id)), 'name': name} for shelter_id, name in shelters]

        return shelters_list
    