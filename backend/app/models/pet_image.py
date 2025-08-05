from sqlalchemy.dialects.mysql import BINARY, ENUM
from app import db
from sqlalchemy import DateTime

import uuid


class PetImage(db.Model):
    __tablename__ = 'pet_images'

    pet_image_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    image_url = db.Column(db.String(255), nullable=False)

    uploaded_at = db.Column(DateTime, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False)

    pet_id = db.Column(
        BINARY(16),
        db.ForeignKey("pets.pet_id"),
        nullable=True
    )

    def __repr__(self):
        return f"<PetImage {self.image_url}>"
