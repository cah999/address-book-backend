import logging

from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from app.dependencies import UOWDependency
from schemas.users import UserSchema, UserOptionalSchema, UserInfoSchema, UserFullSchema
from services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserInfoSchema])
async def get_users(uow: UOWDependency):
    return await UsersService().get_users(uow)


@router.get("/{user_id}", response_model=UserFullSchema)
async def get_user(user_id: int, uow: UOWDependency):
    return await UsersService().get_user(user_id, uow)


@router.post("", response_model=int)
async def create_user(user_data: UserSchema, uow: UOWDependency):
    return await UsersService().create_user(user_data, uow)


@router.put("/{user_id}", )
async def update_user(user_id: int, user_data: UserSchema, uow: UOWDependency):
    await UsersService().update_user(user_id, user_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully updated"})


@router.patch("/{user_id}")
async def patch_user(user_id: int, user_data: UserOptionalSchema, uow: UOWDependency):
    await UsersService().patch_user(user_id, user_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully patched"})


@router.delete("/{user_id}")
async def delete_user(user_id: int, uow: UOWDependency):
    await UsersService().delete_user(user_id, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully deleted"})
