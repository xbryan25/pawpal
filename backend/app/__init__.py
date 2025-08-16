from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from .extensions import db

from .config import Config

from .services import configure_cloudinary

jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    configure_cloudinary(app)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app, origins='*')

    # from app.models import User, Shelter

    from .routes import user_bp, shelter_bp, pet_bp, species_bp, breed_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(shelter_bp, url_prefix='/shelter')
    app.register_blueprint(pet_bp, url_prefix='/pets')
    app.register_blueprint(species_bp, url_prefix='/species')
    app.register_blueprint(breed_bp, url_prefix='/breed')

    return app
