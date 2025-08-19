from flask import jsonify
from app.models import User, Pet, AdoptionApplication, ApplicationStatusEnum
from app.extensions import db
import uuid
from datetime import datetime

class PetService:

    @staticmethod
    def adopt_pet(user_id, pet_id):

        adoption_application = PetService.check_if_user_has_adoption_application(user_id, pet_id)

        if adoption_application and adoption_application.status.value in ['cancelled', 'rejected']:
            adoption_application.status = ApplicationStatusEnum.pending
            adoption_application.application_date = datetime.now()
        elif adoption_application and adoption_application.status.value == 'approved':
            raise ValueError("This application has already been approved.")
        else:

            new_adoption_application = AdoptionApplication(
                status="pending",
                application_date=datetime.now(),
                user_id=user_id,
                pet_id=pet_id,
            )

            db.session.add(new_adoption_application)

        db.session.commit()

    @staticmethod
    def cancel_pet_adoption(user_id, pet_id):

        adoption_application = PetService.check_if_user_has_adoption_application(user_id, pet_id)

        if adoption_application and adoption_application.status == 'cancelled':
            raise ValueError("This application has already been cancelled.")
        else:
            adoption_application.status = 'cancelled'

        db.session.commit()

    @staticmethod
    def check_if_user_has_adoption_application(user_id, pet_id):

        adoption_application = AdoptionApplication.query.filter(
            AdoptionApplication.user_id == user_id,
            AdoptionApplication.pet_id == pet_id,
        ).first()

        if adoption_application:
            return adoption_application
        else:
            return False