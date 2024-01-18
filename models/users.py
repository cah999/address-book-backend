from typing import Optional, get_args

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.users import Gender


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str]
    gender: Mapped[Gender]
    address: Mapped[Optional[str]]

    phones = relationship("Phones", back_populates="user", cascade="all, delete")
    emails = relationship("Emails", back_populates="user", cascade="all, delete")
