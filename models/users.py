import datetime
from typing import Optional, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from models.emails import Emails
from models.phones import Phones
from schemas.users import Gender


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fullName: Mapped[str]
    gender: Mapped[Gender]
    birthDate: Mapped[datetime.date]
    address: Mapped[Optional[str]]

    phones: Mapped[List["Phones"]] = relationship("Phones", back_populates="user", cascade="all, delete")
    emails: Mapped[List["Emails"]] = relationship("Emails", back_populates="user", cascade="all, delete")
