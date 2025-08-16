from app.extensions import db
from sqlalchemy.dialects.mysql import BINARY, ENUM
from sqlalchemy import DateTime

import uuid


class Shelter(db.Model):
    __tablename__ = 'shelters'

    shelter_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(11), unique=True, nullable=False)
    created_at = db.Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Shelter {self.name} ({self.shelter_id})>"
