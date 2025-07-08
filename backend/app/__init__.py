from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from .config import Config

from .services.cloudinary_service import configure_cloudinary

db = SQLAlchemy()
jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    configure_cloudinary(app)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app, origins='*')

    # from app.models import User, Shelter

    from .routes import user_bp, shelter_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(shelter_bp, url_prefix='/shelter')

    return app
