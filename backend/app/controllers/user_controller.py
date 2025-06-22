from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import authenticate_user


def login_controller():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
