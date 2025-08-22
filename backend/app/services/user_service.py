from flask import jsonify

from app.models.user import User
from app.extensions import db

from datetime import datetime
import uuid

import cloudinary.uploader


class UserService:

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def get_user_role(user_id):
        user = User.query.filter(User.user_id == user_id).first()

        if user:
            role = user.role
            return role.value
        else:
            return None
        
    @staticmethod
    def get_shelter_id_from_shelter_staff(user_id):
        user = User.query.filter(User.user_id == user_id).first()

        if user:
            shelter_id = user.shelter_id
            return shelter_id
        else:
            return None
        
    @staticmethod
    def user_signup(new_user_data, new_user_image):

        if User.query.filter_by(email=new_user_data["email"]).first():
            return jsonify({"error": "Email already exists"}), 409
        
        user_image = new_user_image['selectedImage']
        
        result = cloudinary.uploader.upload(user_image, public_id=f"{str(uuid.uuid4())}")   

        new_user = User(
            name=f"{new_user_data['firstName']} {new_user_data['lastName']}",
            gender=new_user_data["gender"],
            address=new_user_data["address"],
            phone_number=new_user_data["phoneNumber"],
            birth_date=datetime.strptime(new_user_data["birthDate"], "%Y-%m-%d").date(),
            email=new_user_data["email"],
            role=new_user_data["role"],
            profile_url=result["secure_url"],
            shelter_id=None if new_user_data["role"] == "adopter" else uuid.UUID(new_user_data.get("shelterId")).bytes
        )

        # password.setter gets triggered
        new_user.password = new_user_data["password"]

        db.session.add(new_user)
        db.session.commit()