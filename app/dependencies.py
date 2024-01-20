from typing import Annotated

from fastapi import Depends

from exceptions.notfound import UserNotFound
from services.users import UsersService
from utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]


async def validate_user(user_id: int, uow: UOWDependency):
    user = await UsersService().get_user(user_id, uow)
    if user is None:
        raise UserNotFound(user_id)
    return user
