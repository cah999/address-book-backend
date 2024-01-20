from typing import get_args

from sqlalchemy import ForeignKey, UUID, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from schemas.emails import EmailType


class Emails(Base):
    __tablename__ = "emails"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    emailType: Mapped[EmailType]
    email: Mapped[str] = mapped_column(nullable=False)

    user = relationship("Users", back_populates="emails", cascade="all, delete")
