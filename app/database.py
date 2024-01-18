from os import getenv

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(f"postgresql+asyncpg://"
                             f"{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@"
                             f"{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
