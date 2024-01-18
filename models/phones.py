from typing import get_args

from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.phones import PhoneType


class Phones(Base):
    __tablename__ = "phones"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    phone_type: Mapped[PhoneType]
    phone: Mapped[str] = mapped_column(String(12))

    user = relationship("Users", back_populates="phones", cascade="all, delete")
