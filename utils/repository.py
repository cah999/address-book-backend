from abc import ABC, abstractmethod


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
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, item_id: int):
        raise NotImplementedError
