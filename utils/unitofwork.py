import logging
from abc import ABC, abstractmethod

from fastapi import HTTPException, status

from database.database import async_session_maker
from repositories.users import UsersRepository


class IUnitOfWork(ABC):
    users: UsersRepository

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker
        self.logger = logging.getLogger(__name__)

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
