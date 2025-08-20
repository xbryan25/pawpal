
from app.models import AdoptionApplication, Pet, Shelter, PetImage, User

import uuid

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
    def check_if_user_has_adoption_application(user_id, pet_id):

        adoption_application = AdoptionApplication.query.filter(
            AdoptionApplication.user_id == user_id,
            AdoptionApplication.pet_id == pet_id,
        ).first()

        if adoption_application:
            return adoption_application
        else:
            return False
        
