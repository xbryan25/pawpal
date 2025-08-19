from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app.services import UserService
from app.models.user import User
from app.models.shelter import Shelter
from app.extensions import db

from datetime import datetime
import uuid


def user_login_controller():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    login_type = data.get("loginType")

    user = UserService.authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials."}), 401
    elif user.role.value != login_type:
        return jsonify({"error": "Invalid login type."}), 401

    uuid_str = str(uuid.UUID(bytes=user.user_id))
    access_token = create_access_token(identity=uuid_str)

    user_role = get_user_role(email)

    return jsonify({
        "access_token": access_token,
        "user_role": user_role,
        "user_id": uuid_str
    }), 200


# TODO: I think this should be in another file, also add error handling
def get_user_role(email):
    user = User.query.filter_by(email=email).first()

    if user:
        role = user.role
        return role.value
    else:
        return None

def user_signup_controller():
    data = request.json

    # Check if email already exists
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 409

    # Optional: validate required fields here

    try:
        new_user = User(
            name=f"{data['firstName']} {data['lastName']}",
            gender=data["gender"],
            address=data["address"],
            phone_number=data["phoneNumber"],
            birth_date=datetime.strptime(data["birthDate"], "%Y-%m-%d").date(),
            email=data["email"],
            role=data["role"],
            profile_url="https://placehold.co/128x128",
            shelter_id=None if data["role"] == "adopter" else uuid.UUID(data.get("shelterId")).bytes
        )

        # password.setter gets triggered
        new_user.password = data["password"]

        # test_shelter = Shelter(
        #     name=f"Test Shelter",
        #     email="test@email.com",
        #     address="Test Address",
        #     phone_number="09865698651",
        #     created_at=datetime.now(),
        # )
        #
        # db.session.add(test_shelter)
        # db.session.commit()

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
