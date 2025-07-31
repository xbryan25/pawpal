from app import db
from sqlalchemy.dialects.mysql import BINARY, ENUM
from sqlalchemy import Date

import uuid

from app.models.enums import SexEnum, PetStatusEnum


class Pet(db.Model):
    __tablename__ = 'pets'

    pet_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(Date, nullable=False)
    sex = db.Column(ENUM(SexEnum, name="sex_enum", values_callable=lambda x: [e.value for e in x]),
                    nullable=False)
    status = db.Column(ENUM(PetStatusEnum, name="pet_status_enum", values_callable=lambda x: [e.value for e in x]),
                       nullable=False)
    description = db.Column(db.String(255), nullable=False)

    breed_id = db.Column(
        BINARY(16),
        db.ForeignKey("breeds.breed_id"),
        nullable=True
    )

    species_id = db.Column(
        BINARY(16),
        db.ForeignKey("species.species_id"),
        nullable=True
    )

    shelter_id = db.Column(
        BINARY(16),
        db.ForeignKey("shelters.shelter_id"),
        nullable=True
    )


    def __repr__(self):
        return f"<Pet {self.name}>"