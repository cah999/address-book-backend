from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.dependencies import UOWDependency, validate_user
from schemas.users import UserSchema, UserOptionalSchema, UserInfoSchema, UserFullSchema
from services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserInfoSchema])
async def get_users(session: UOWDependency):
    return await UsersService().get_users(session)


@router.get("/{user_id}", response_model=UserFullSchema)
async def get_user(user: Annotated[UserFullSchema, Depends(validate_user)], session: UOWDependency):
    return await UsersService().get_full_user(user, session)


@router.post("", response_model=int)
async def create_user(user_data: UserSchema, session: UOWDependency):
    return await UsersService().create_user(user_data, session)


@router.put("/{user_id}")
async def update_user(user: Annotated[UserFullSchema, Depends(validate_user)], user_data: UserSchema,
                      session: UOWDependency):
    await UsersService().update_user(user.id, user_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully updated"})


@router.patch("/{user_id}")
async def patch_user(user: Annotated[UserFullSchema, Depends(validate_user)], user_data: UserOptionalSchema,
                     session: UOWDependency):
    await UsersService().patch_user(user.id, user_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully patched"})


@router.delete("/{user_id}")
async def delete_user(user: Annotated[UserFullSchema, Depends(validate_user)], session: UOWDependency):
    await UsersService().delete_user(user.id, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "User successfully deleted"})
