from app.extensions import db
from sqlalchemy.dialects.mysql import BINARY, ENUM
from sqlalchemy import Date

from werkzeug.security import generate_password_hash, check_password_hash

import uuid

from app.models.enums import GenderEnum, RoleEnum


class User(db.Model):
    __tablename__ = 'users'

    _password = db.Column("password", db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return check_password_hash(self._password, plaintext)

    user_id = db.Column(BINARY(16), primary_key=True, default=lambda: uuid.uuid4().bytes)

    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(ENUM(GenderEnum, name="gender_enum", values_callable=lambda x: [e.value for e in x]),
                       nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(11), unique=True, nullable=False)
    birth_date = db.Column(Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    role = db.Column(ENUM(RoleEnum, name="role_enum", values_callable=lambda x: [e.value for e in x]),
                       nullable=False)
    profile_url = db.Column(db.String(255), nullable=False)

    shelter_id = db.Column(
        BINARY(16),
        db.ForeignKey("shelters.shelter_id"),
        nullable=True
    )

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"