from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.phones import PhoneType


class Phones(Base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    phoneType: Mapped[PhoneType]
    phone: Mapped[str] = mapped_column(String(12))

    user = relationship("Users", back_populates="phones", cascade="all, delete")
