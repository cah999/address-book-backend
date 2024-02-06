import enum

import sqlalchemy
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.settings import settings

print(
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
engine = create_async_engine(f"postgresql+asyncpg://"
                             f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
                             f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: sqlalchemy.Enum(enum.Enum, values_callable=lambda x: [i.value for i in x]),
    }
