from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .config import Config

from .services.cloudinary_service import configure_cloudinary

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    configure_cloudinary(app)

    CORS(app, origins='*')

    db.init_app(app)

    return app
