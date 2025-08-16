from sqlalchemy.dialects.mysql import BINARY, ENUM
from app.extensions import db

import uuid


class Species(db.Model):
    __tablename__ = 'species'

    species_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)
    species_name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"<Species {self.species_name}>"
