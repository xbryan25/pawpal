import enum


class GenderEnum(enum.Enum):
    male = "male"
    female = "female"
    others = "others"
    prefer_not_to_say = "prefer not to say"


class RoleEnum(enum.Enum):
    adopter = "adopter"
    shelter_staff = "shelter_staff"
    admin = "admin"


class SexEnum(enum.Enum):
    male = "male"
    female = "female"


class PetStatusEnum(enum.Enum):
    available = "available"
    adopted = "adopted"
    unavailable = "unavailable"


class ApplicationStatusEnum(enum.Enum):
    approved = "approved"
    rejected = "rejected"
    pending = "pending"
    cancelled = "cancelled"
