import enum
import re
from typing import Optional

from pydantic import BaseModel, field_validator


class EmailType(enum.Enum):
    personal = "личная"
    work = "рабочая"


class EmailAddSchema(BaseModel):
    emailType: EmailType
    email: str

    @field_validator("email")
    def email_validator(cls, email):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email is not valid")
        return email


class EmailSchema(EmailAddSchema):
    id: int
    userId: int

    class Config:
        from_attributes = True


class EmailInfoSchema(EmailAddSchema):
    id: int

    class Config:
        from_attributes = True


class EmailOptionalSchema(EmailAddSchema):
    emailType: Optional[EmailType] = None
    email: Optional[str] = None
