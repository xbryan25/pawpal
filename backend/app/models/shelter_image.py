from app import db
from sqlalchemy import DateTime

import uuid


class ShelterImage(db.Model):
    __tablename__ = 'shelter_image'

    shelter_image_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    image_url = db.Column(db.String(255), nullable=False)

    uploaded_at = db.Column(DateTime, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False)

    shelter_id = db.Column(
        BINARY(16),
        db.ForeignKey("shelters.shelter_id"),
        nullable=True
    )

    def __repr__(self):
        return f"<ShelterImage {self.image_url}>"
