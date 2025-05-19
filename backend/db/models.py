"""DB models for the application."""

from sqlalchemy import Column, Integer, String, ForeignKey
from email_validator.rfc_constants import EMAIL_MAX_LENGTH

from .base import Base


class User(Base):
    """Модель пользователя в БД."""

    email = Column(
        String(EMAIL_MAX_LENGTH),
        unique=True,
        nullable=False,
        index=True,
    )
    password = Column(
        String,
        nullable=False,
    )

    def __repr__(self):
        return "Пользователь {id}: {email}".format(
            id=self.id,
            email=self.email,
        )
