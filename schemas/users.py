import enum
from datetime import date
from typing import Optional

from pydantic import BaseModel, field_validator


class Gender(enum.Enum):
    male = "мужской"
    female = "женский"


class UserSchema(BaseModel):
    full_name: str
    gender: Gender
    birth_date: date
    address: Optional[str]

    @field_validator("full_name")
    def full_name_validator(cls, value):
        if not value.isalpha():
            raise ValueError("Имя и фамилия должны состоять только из букв")
        if len(value.split()) != 3:
            raise ValueError("Имя, фамилия и отчество должны быть указаны")
        return value

    class Config:
        from_attributes = True
