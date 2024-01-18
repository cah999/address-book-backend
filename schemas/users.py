import enum
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Gender(enum.Enum):
    male = "мужской"
    female = "женский"


class UserSchema(BaseModel):
    full_name: str
    gender: Gender
    birth_date: date
    address: Optional[str]
