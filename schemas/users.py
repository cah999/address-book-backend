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
            raise ValueError("Имя, фамилия и отчество должны быть указаны")
        return value

    class Config:
        from_attributes = True
