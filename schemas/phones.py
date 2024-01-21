import enum
import re
from typing import Optional

from pydantic import BaseModel, field_validator


class PhoneType(enum.Enum):
    city = "городской"
    mobile = "мобильный"


class PhoneAddSchema(BaseModel):
    phoneType: PhoneType
    phone: str

    @field_validator("phone")
    def phone_validator(cls, v):
        if not re.match(r"^\+\d{11}$", v):
            raise ValueError("Invalid phone number. Example: +79999999999")
        return v


class PhoneInfoSchema(PhoneAddSchema):
    id: int

    class Config:
        from_attributes = True


class PhoneSchema(PhoneAddSchema):
    id: int
    userId: int

    class Config:
        from_attributes = True


class PhoneOptionalSchema(PhoneAddSchema):
    phoneType: Optional[PhoneType] = None
    phone: Optional[str] = None
