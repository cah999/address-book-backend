from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from utils.repository import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> str:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def get_item_by_field(self, field: str, value: str):
        stmt = select(self.model).where(getattr(self.model, field) == value)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def update_one(self, item_id: id, data: dict, **filter_by) -> int:
        stmt = update(self.model).values(**data).filter_by(**filter_by).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_one(self, item_id: int):
        stmt = select(self.model).where(self.model.id == item_id)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()
