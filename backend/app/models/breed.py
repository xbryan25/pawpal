from sqlalchemy.dialects.mysql import BINARY, ENUM
from app import db

import uuid


class Breed(db.Model):
    __tablename__ = 'breeds'

    breed_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)
    breed_name = db.Column(db.String(30), unique=True, nullable=False)

    species_id = db.Column(
        BINARY(16),
        db.ForeignKey("species.species_id"),
        nullable=True
    )

    def __repr__(self):
        return f"<Breed {self.name}>"
