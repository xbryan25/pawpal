from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app.services import UserService
from app.extensions import db

import uuid


class UserController:

    @staticmethod
    def user_login_controller():
        data = request.json
        email = data.get("email")
        password = data.get("password")
        login_type = data.get("loginType")

        try:
            user = UserService.authenticate_user(email, password)
            

            if not user:
                return jsonify({"error": "Invalid credentials."}), 401
            elif user.role.value != login_type:
                return jsonify({"error": "Invalid login type."}), 401
            
            user_id = user.user_id
            user_id_str = str(uuid.UUID(bytes=user_id))
            access_token = create_access_token(identity=user_id_str)

            user_role = UserService.get_user_role(user_id)
            shelter_id = UserService.get_shelter_id_from_shelter_staff(user_id)
            profile_image_url = UserService.get_user_profile_image_url(user_id)

            return jsonify({
                "accessToken": access_token,
                "userRole": user_role,
                "userId": user_id_str,
                "shelterId": str(uuid.UUID(bytes=shelter_id)) if shelter_id else None,
                "profileImageUrl": profile_image_url
            }), 200
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def user_signup_controller():
        new_user_data = request.form
        new_user_image = request.files
        
        try:
            UserService.user_signup(new_user_data, new_user_image)
            return jsonify({"message": "Account created successfully. Please login."}), 201

        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
