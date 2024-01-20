import logging

from fastapi import HTTPException

from schemas.users import UserSchema, UserOptionalSchema, UserInfoSchema
from fastapi import status
from utils.unitofwork import IUnitOfWork


class UsersService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def get_users(self, uow: IUnitOfWork) -> list[UserInfoSchema]:
        async with uow:
            return await uow.users.find_all(UserInfoSchema)

    async def get_user(self, user_id: int, uow: IUnitOfWork) -> UserInfoSchema:
        async with uow:
            user = await uow.users.find_one(user_id, UserInfoSchema)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
        return user

    async def create_user(self, user_data: UserSchema, uow: IUnitOfWork) -> int:
        self.logger.info(f"Creating user with data: {user_data}")
        async with uow:
            user_id = await uow.users.add_one(user_data.model_dump())
            await uow.commit()
        self.logger.info(f"User created with id: {user_id}")
        return int(user_id)

    async def update_user(self, user_id: int, user_data: UserSchema, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Updating user {user_id} with new data: {user_data}")
        async with uow:
            res = await uow.users.update_one(user_id, user_data.model_dump(), id=user_id)
            if res is None:
                self.logger.error(f"User with id: {user_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
            await uow.commit()
        self.logger.info(f"User with id: {user_id} updated")
        return True

    async def patch_user(self, user_id: int, user_data: UserOptionalSchema, uow: IUnitOfWork) -> bool:
        user_dict = user_data.model_dump(exclude_unset=True)
        self.logger.info(f"Updating user {user_id} with new data: {user_dict}")
        if all(value is None for value in user_dict.values()) or len(user_dict) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found fields for update")
        async with uow:
            user = await uow.users.update_one(user_id, user_dict, id=user_id)
            if user is None:
                self.logger.error(f"User with id: {user_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
            await uow.commit()
        self.logger.info(f"User with id: {user_id} updated")
        return True

    async def delete_user(self, user_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Deleting user with id: {user_id}")
        async with uow:
            res = await uow.users.delete_one(user_id)
            if res is None:
                self.logger.error(f"User with id: {user_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
            await uow.commit()
        self.logger.info(f"User with id: {user_id} deleted")
        return True
