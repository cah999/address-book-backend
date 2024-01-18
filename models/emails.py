import enum

from sqlalchemy import ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from schemas.emails import EmailType


class Emails(Base):
    __tablename__ = "emails"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    email_type: Mapped[EmailType]
    email: Mapped[str] = mapped_column(nullable=False)

    user = relationship("Users", back_populates="emails")

    def to_read_model(self) -> ...:
        ...
