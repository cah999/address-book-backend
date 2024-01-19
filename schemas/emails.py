import enum

from pydantic import BaseModel


class EmailType(enum.Enum):
    personal = "личная"
    work = "рабочая"


class EmailSchema(BaseModel):
    userId: int
    emailType: EmailType
    email: str

    class Config:
        from_attributes = True
