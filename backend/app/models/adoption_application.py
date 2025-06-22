from app import db
from sqlalchemy.dialects.mysql import BINARY, ENUM
from sqlalchemy import DateTime

import uuid

from app.models.enums import ApplicationStatusEnum


class AdoptionApplications(db.Model):
    __tablename__ = 'adoption_applications'

    aa_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    status = db.Column(ENUM(ApplicationStatusEnum, name="application_status_enum",
                            values_callable=lambda x: [e.value for e in x]),
                       nullable=False)

    application_date = db.Column(DateTime, nullable=False)
    decision_date = db.Column(DateTime, nullable=False)

    user_id = db.Column(
        BINARY(16),
        db.ForeignKey("users.user_id"),
        nullable=True
    )

    pet_id = db.Column(
        BINARY(16),
        db.ForeignKey("pets.pet_id"),
        nullable=True
    )

    def __repr__(self):
        return f"<AdoptionApplication {self.aa_id}>"
    