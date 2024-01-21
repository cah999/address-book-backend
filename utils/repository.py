from abc import abstractmethod, ABC
from typing import Type

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, item_id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_item_by_field(self, field: str, value: str):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, schema: Type[BaseModel]):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, item_id: int, schema: Type[BaseModel]):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> str:
        stmt = insert(self.model).values(**data).returning(self.model.id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def get_item_by_field(self, field: str, value: str):
        stmt = select(self.model).where(getattr(self.model, field) == value)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def find_all(self, schema: Type[BaseModel], **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [schema.model_validate(row[0]) for row in res.all()]
        return res

    async def update_one(self, item_id: id, data: dict, **filter_by) -> int | None:
        stmt = update(self.model).values(**data).filter_by(**filter_by).returning(self.model.id)
        res = await self.session.execute(stmt)
        try:
            return res.scalar_one()
        except NoResultFound:
            return None

    async def find_one(self, item_id: int, schema: Type[BaseModel]):
        stmt = select(self.model).where(self.model.id == item_id)
        res = await self.session.execute(stmt)
        user = res.scalar_one_or_none()
        if user is None:
            return None
        return schema.model_validate(user)

    async def delete_one(self, item_id: int):
        stmt = delete(self.model).where(self.model.id == item_id).returning(self.model.id)
        res = await self.session.execute(stmt)
        try:
            return res.scalar_one()
        except NoResultFound:
            return None
