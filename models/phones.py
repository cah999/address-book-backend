import enum

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class PhoneType(enum.Enum):
    city = "городской"
    mobile = "мобильный"


class Phones(Base):
    __tablename__ = "phones"

    user_id: Mapped[UUID] = mapped_column(UUID(), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    phone_type: Mapped[PhoneType]
    phone: Mapped[str] = mapped_column(String(11))

    user = relationship("Users", back_populates="phones")

    def to_read_model(self) -> ...:
        ...
