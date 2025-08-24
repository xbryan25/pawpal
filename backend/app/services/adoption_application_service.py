
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
                "adopterAcceptedApplications": application_counts.approved,
                "adopterProfileImageUrl": adopter.profile_url
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

    @staticmethod
    def reject_application(aa_id):

        adoption_application = AdoptionApplication.query.filter(AdoptionApplication.aa_id == aa_id).first()

        adoption_application.status = ApplicationStatusEnum.rejected
        adoption_application.decision_date = datetime.now()

        db.session.commit()

    @staticmethod
    def get_applications_frequency(selected_range, first_value, shelter_id):

        applications_frequency_list = []

        if selected_range == 'monthly':

            months = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
            
            current_month_index = months.index(first_value[:-5]) + 1
            current_year = int(first_value[-5:])

            # 12 for 12 months
            for _ in range(12):
                
                start_date = datetime(current_year, current_month_index, 1)

                if current_month_index == 12:
                    current_month_index = 1
                    current_year += 1
                else:
                    current_month_index += 1

                end_date = datetime(current_year, current_month_index, 1)

                if not shelter_id:

                    frequency = AdoptionApplication.query.filter(AdoptionApplication.application_date >= start_date, 
                                                                AdoptionApplication.application_date < end_date).count()
                    
                else:

                    frequency = db.session.query(db.func.count(AdoptionApplication.aa_id)).join(Pet, 
                                                                                           AdoptionApplication.pet_id == Pet.pet_id).filter(Pet.shelter_id == shelter_id,
                                                                                                                                 AdoptionApplication.application_date >= start_date, AdoptionApplication.application_date < end_date).scalar()
                    

                applications_frequency_list.append(frequency)

        else:
            current_year = int(first_value)

            # 5 for 5 years
            for _ in range(5):
                
                start_date = datetime(current_year, 1, 1)

                current_year += 1

                end_date = datetime(current_year, 1, 1)

                if not shelter_id:

                    frequency = AdoptionApplication.query.filter(AdoptionApplication.application_date >= start_date, 
                                                                AdoptionApplication.application_date < end_date).count()
                    
                else:

                    frequency = db.session.query(db.func.count(AdoptionApplication.aa_id)).join(Pet, 
                                                                                           AdoptionApplication.pet_id == Pet.pet_id).filter(Pet.shelter_id == shelter_id,
                                                                                                                                 AdoptionApplication.application_date >= start_date, AdoptionApplication.application_date < end_date).scalar()


                applications_frequency_list.append(frequency)

        return applications_frequency_list


    @staticmethod
    def get_application_status_frequency(shelter_id):

        application_status_frequency_list = []

        status = ['approved', 'rejected', 'pending']

        for one_status in status:

            frequency = db.session.query(db.func.count(AdoptionApplication.aa_id)).join(Pet, 
                                                                                        AdoptionApplication.pet_id == Pet.pet_id).filter(Pet.shelter_id == shelter_id, AdoptionApplication.status == one_status).scalar()

            application_status_frequency_list.append(frequency)
        

        return application_status_frequency_list