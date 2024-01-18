import enum
import re
from uuid import UUID

from pydantic import BaseModel, field_validator


class PhoneType(enum.Enum):
    city = "городской"
    mobile = "мобильный"


class PhoneSchema(BaseModel):
    user_id: UUID
    phone_type: PhoneType
    phone: str

    @field_validator("phone")
    def phone_validator(cls, v):
        if not re.match(r"^\+\d{11}$", v):
            raise ValueError("Указан неверный формат номера телефона. Пример: +79991234567")
        return v
