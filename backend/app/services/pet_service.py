from flask import jsonify
from app.models import User, Pet, AdoptionApplication
from app.extensions import db
import uuid
from datetime import datetime

def adopt_pet(user_id, pet_id):

    new_adoption_application = AdoptionApplication(
        status="pending",
        application_date=datetime.now(),
        user_id=user_id,
        pet_id=pet_id,
    )

    db.session.add(new_adoption_application)
    db.session.commit()

def cancel_pet_adoption(adoption_application):
    adoption_application.status = 'cancelled'
    db.session.commit()


def check_if_pet_has_been_adopter_by_user(user_id, pet_id):

    adoption_application = AdoptionApplication.query.filter(
        AdoptionApplication.user_id == user_id,
        AdoptionApplication.pet_id == pet_id,
        AdoptionApplication.status != "cancelled"
    ).first()

    if adoption_application:
        return adoption_application
    else:
        return False