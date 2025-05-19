"""Pydantic модели для работы с пользователями."""

import re

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from pydantic.v1.utils import validate_field_name
from starlette.status import HTTP_400_BAD_REQUEST

import settings


class UserRead:
    """Модель чтения пользователя."""

    id: int
    name: str
    email: EmailStr


class UserCreate(BaseModel):
    """Модель создания пользователя."""

    email: EmailStr
    name: str
    password: str

    @validate_field_name("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        """Валидация пароля."""
        if len(password) < settings.PASSWORD_MIN_LENGTH:
            raise ValueError(
                "Пароль не должен быть менее {pwd} символов.".format(
                    pwd=settings.PASSWORD_MIN_LENGTH
                )
            )
        if len(password) > settings.PASSWORD_MAX_LENGTH:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Пароль должен быть не более {pwd} символов.".format(
                    pwd=settings.PASSWORD_MAX_LENGTH
                ),
            )
        if re.search(r"[0-9]", password) is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Пароль должен содержать хотя бы одну цифру.",
            )
        if re.search(r"[A-Z]", password) is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Пароль должен содержать хотя бы одну заглавную букву.",
            )
        if re.search(r"[a-z]", password) is None:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Пароль должен содержать хотя бы одну строчную букву.",
            )
