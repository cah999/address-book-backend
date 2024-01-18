import enum
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from schemas.phones import PhoneType


class Phones(Base):
    __tablename__ = "phones"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    phone_type: Mapped[PhoneType]
    phone: Mapped[str] = mapped_column(String(11))

    user = relationship("Users", back_populates="phones")

    def to_read_model(self) -> ...:
        ...
