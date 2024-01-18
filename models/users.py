import enum
import uuid
from typing import Optional

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from schemas.users import Gender


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True, default=uuid.uuid4())
    full_name: Mapped[str]
    gender: Mapped[Gender]
    address: Mapped[Optional[str]]

    phones = relationship("Phones", back_populates="user")
    emails = relationship("Emails", back_populates="user")

    def to_read_model(self) -> ...:
        ...
