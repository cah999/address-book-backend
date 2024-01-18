import enum

from pydantic import BaseModel


class EmailType(enum.Enum):
    personal = "личная"
    work = "рабочая"


class EmailSchema(BaseModel):
    user_id: int
    email_type: EmailType
    email: str

    class Config:
        from_attributes = True
