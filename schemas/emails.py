import enum
from typing import Optional

from pydantic import BaseModel


class EmailType(enum.Enum):
    personal = "личная"
    work = "рабочая"


class EmailAddSchema(BaseModel):
    # todo validate
    emailType: EmailType
    email: str


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
