"""Базовая модель для всех моделей базы данных."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, Integer, String


class PreBase:
    """Модель для всех моделей базы данных."""

    @declared_attr
    def __tablename__(cls) -> str:
        """Имя таблицы в базе данных."""
        return cls.__name__.lower() + "s"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )


Base = declarative_base(cls=PreBase)
