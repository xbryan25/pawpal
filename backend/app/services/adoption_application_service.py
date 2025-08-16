from app.models import AdoptionApplication


def get_num_of_adoption_applications(pet_id):

    num_of_adoption_applications = AdoptionApplication.query.filter(AdoptionApplication.pet_id == pet_id, AdoptionApplication.status != "cancelled").count()

    return num_of_adoption_applications
