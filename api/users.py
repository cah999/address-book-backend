from fastapi import APIRouter

from app.dependencies import UOWDependency
from services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("")
async def get_users(uow: UOWDependency):
    return await UsersService().get_users(uow)
