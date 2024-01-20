import enum
from datetime import date
from typing import Optional

from pydantic import BaseModel, field_validator


class Gender(enum.Enum):
    male = "мужской"
    female = "женский"


class UserSchema(BaseModel):
    fullName: str
    gender: Gender
    birthDate: date
    address: Optional[str]

    @field_validator("fullName")
    def full_name_validator(cls, value):
        if len(value.split()) != 3:
            raise ValueError("full name must contain 3 words")
        if not value.replace(" ", "").isalpha():
            raise ValueError("full name must contain only letters")
        if not value.istitle():
            raise ValueError("full name must be in title case")
        return value

    @field_validator("birthDate")
    def birth_date_validator(cls, value):
        if value > date.today():
            raise ValueError("birth date must be in past")
        if value.year < 1900:
            raise ValueError("birth date must be after 1900")
        return value

    @field_validator("address")
    def address_validator(cls, value):
        if value is not None and len(value) > 255:
            raise ValueError("address must be less than 255 characters")
        return value


class UserInfoSchema(UserSchema):
    id: int

    class Config:
        from_attributes = True


class UserOptionalSchema(UserSchema):
    fullName: Optional[str] = None
    gender: Optional[Gender] = None
    birthDate: Optional[date] = None
    address: Optional[str] = None
