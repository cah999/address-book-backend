import uuid
from abc import ABC, abstractmethod

from fastapi import HTTPException
from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, item_id: uuid, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_item_by_field(self, field: str, value: str):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> str:
        async with async_session_maker() as session:
            try:
                stmt = insert(self.model).values(**data).returning(self.model.id)
                res = await session.execute(stmt)
            except IntegrityError as e:
                await session.rollback()
                raise HTTPException(status_code=400, detail=str(e.orig))
            else:
                await session.commit()
                return res.scalar_one()

    async def get_item_by_field(self, field: str, value: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(getattr(self.model, field) == value)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def update_one(self, item_id: uuid, data: dict) -> int:
        async with async_session_maker() as session:
            try:
                # noinspection PyTypeChecker
                stmt = update(self.model).where(self.model.id == item_id).values(**data).returning(self.model.id)
                res = await session.execute(stmt)
            except IntegrityError as e:
                await session.rollback()
                raise HTTPException(status_code=400, detail=str(e.orig))
            else:
                await session.commit()
                return res.scalar_one()
