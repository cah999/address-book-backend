import enum
from uuid import UUID

from pydantic import BaseModel, EmailStr


class EmailType(enum.Enum):
    personal = "личная"
    work = "рабочая"


class EmailSchema(BaseModel):
    user_id: UUID
    email_type: EmailType
    email: EmailStr

    class Config:
        orm_mode = True
