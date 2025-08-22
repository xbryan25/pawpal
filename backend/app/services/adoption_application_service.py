
from app.models import AdoptionApplication, Pet, Shelter, PetImage, User, ApplicationStatusEnum, PetStatusEnum
from app.extensions import db

import uuid
from sqlalchemy import func, case, cast, Integer
from datetime import datetime

class AdoptionApplicationService:

    @staticmethod
    def get_num_of_adoption_applications(pet_id):

        num_of_adoption_applications = AdoptionApplication.query.filter(AdoptionApplication.pet_id == pet_id, AdoptionApplication.status != "cancelled").count()

        return num_of_adoption_applications

    @staticmethod
    def get_adopter_applications(user_id):

        adoption_applications = AdoptionApplication.query.filter(AdoptionApplication.user_id == user_id).all()

        adoption_applications_result_list = []

        for adoption_application in adoption_applications:
            pet_id = adoption_application.pet_id

            pet_details = Pet.query.filter(Pet.pet_id == pet_id).first()

            shelter_id = pet_details.shelter_id

            shelter_details = Shelter.query.filter(Shelter.shelter_id == shelter_id).first()

            first_pet_image = PetImage.query.filter(PetImage.pet_id == pet_id, PetImage.sort_order == 1).first()

            adoption_application_dict = {
                "petId": str(uuid.UUID(bytes=pet_id)),
                "petFirstImageUrl": first_pet_image.image_url,
                "petName": pet_details.name,
                "shelterName": shelter_details.name,
                "applicationDate": adoption_application.application_date.strftime("%B %d, %Y %I:%M %p"),
                "status": adoption_application.status.value.capitalize()
            }

            adoption_applications_result_list.append(adoption_application_dict)

        return adoption_applications_result_list
    
    @staticmethod
    def get_shelter_applications(shelter_id):

        shelter_applications_result_list = []

        pets_in_shelter = Pet.query.filter(Pet.shelter_id == shelter_id).all()

        for pet in pets_in_shelter:

            adoption_applications = AdoptionApplication.query.filter(AdoptionApplication.pet_id == pet.pet_id).all()

            for adoption_application in adoption_applications:

                user_id = adoption_application.user_id

                user_name, user_profile_url = User.query.with_entities(User.name, User.profile_url).filter(User.user_id == user_id).first()

                pet_id = adoption_application.pet_id

                pet_details = Pet.query.filter(Pet.pet_id == pet_id).first()

                shelter_id = pet_details.shelter_id

                shelter_details = Shelter.query.filter(Shelter.shelter_id == shelter_id).first()

                first_pet_image = PetImage.query.filter(PetImage.pet_id == pet_id, PetImage.sort_order == 1).first()

                adoption_application_dict = {
                    "applicationId": str(uuid.UUID(bytes=adoption_application.aa_id)),
                    "userName": user_name,
                    "userProfileUrl": user_profile_url,
                    "petId": str(uuid.UUID(bytes=pet_id)),
                    "petFirstImageUrl": first_pet_image.image_url,
                    "petName": pet_details.name,
                    "shelterName": shelter_details.name,
                    "applicationDate": adoption_application.application_date.strftime("%B %d, %Y %I:%M %p"),
                    "status": adoption_application.status.value.capitalize()
                }

                shelter_applications_result_list.append(adoption_application_dict)

        return shelter_applications_result_list
    
    @staticmethod
    def check_if_user_has_adoption_application(user_id, pet_id):

        adoption_application = AdoptionApplication.query.filter(
            AdoptionApplication.user_id == user_id,
            AdoptionApplication.pet_id == pet_id,
        ).first()

        if adoption_application:
            return adoption_application
        else:
            return None
    
    @staticmethod
    def get_application_details(aa_id):

        adoption_application = AdoptionApplication.query.filter(AdoptionApplication.aa_id == aa_id).first()

        # Gets both the total applications and approved applications at the same time
        application_counts = (
            AdoptionApplication.query
            .with_entities(
                func.count().label("total"),
                func.sum(case((AdoptionApplication.status == "approved", 1), else_=0)).cast(Integer).label("approved")
            )
            .filter(AdoptionApplication.user_id == adoption_application.user_id)
            .first()
        )

        adopter = User.query.filter(User.user_id == adoption_application.user_id).first()

        selected_pet = Pet.query.filter(Pet.pet_id == adoption_application.pet_id).first()

        pet_first_image_url_row = PetImage.query.with_entities(PetImage.image_url).filter(PetImage.pet_id == adoption_application.pet_id, PetImage.sort_order == 1).first()

        pet_first_image_url = pet_first_image_url_row[0] if pet_first_image_url_row else None

        application_details_dict = {
            "applicationStatus": adoption_application.status.value,

            "adopterDetails": {
                "adopterName": adopter.name,
                "adopterGender": adopter.gender.value.capitalize(),
                "adopterPhoneNumber": adopter.phone_number,
                "adopterBirthDate": adopter.birth_date.strftime("%B %d, %Y"),
                "adopterEmail": adopter.email,
                "adopterTotalApplications": application_counts.total,
                "adopterAcceptedApplications": application_counts.approved
            },

            "petDetails": {
                "petId": str(uuid.UUID(bytes=selected_pet.pet_id)),
                "petName": selected_pet.name,
                "petFirstImageUrl": pet_first_image_url
            }
            
        }

        if application_details_dict:
            return application_details_dict
        else:
            return None
    
    @staticmethod
    def approve_application(aa_id):

        adoption_application = AdoptionApplication.query.filter(AdoptionApplication.aa_id == aa_id).first()

        selected_pet = Pet.query.filter(Pet.pet_id == adoption_application.pet_id).first()

        adoption_applications_for_pet = AdoptionApplication.query.filter(AdoptionApplication.aa_id != aa_id, 
                                                                         AdoptionApplication.pet_id == adoption_application.pet_id, 
                                                                         AdoptionApplication.status == ApplicationStatusEnum.pending).all()

        adoption_application.status = ApplicationStatusEnum.approved
        adoption_application.decision_date = datetime.now()

        for adoption_application_for_pet in adoption_applications_for_pet:
            adoption_application_for_pet.status = ApplicationStatusEnum.rejected
            adoption_application_for_pet.decision_date = datetime.now()

        selected_pet.status = PetStatusEnum.adopted

        db.session.commit()

