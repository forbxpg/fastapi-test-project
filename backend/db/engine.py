"""Модуль для создания движка SQLAlchemy."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

import settings


engine = create_async_engine(
    url=settings.DB_URL,
    echo=settings.DB_ECHO,
    future=True,
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Создает новый объект сессии для работы с БД.

    Используется в качестве зависимости.
    """
    try:
        async with async_session() as session:
            yield session
    finally:
        await session.close()
