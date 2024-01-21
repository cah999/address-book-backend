import logging

from fastapi import HTTPException

from schemas.emails import EmailInfoSchema
from schemas.phones import PhoneInfoSchema
from schemas.users import UserSchema, UserOptionalSchema, UserInfoSchema, UserFullSchema
from fastapi import status
from utils.unitofwork import IUnitOfWork


class UsersService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def get_users(self, uow: IUnitOfWork) -> list[UserInfoSchema]:
        self.logger.info("Getting all users")
        async with uow:
            return await uow.users.find_all(UserInfoSchema)

    async def get_user(self, user_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Getting user with id: {user_id}")
        async with uow:
            return await uow.users.find_one(user_id, UserInfoSchema)

    async def get_full_user(self, user: UserInfoSchema, uow: IUnitOfWork) -> UserFullSchema:
        self.logger.info(f"Getting full user with id: {user.id}")
        async with uow:
            user_dict = user.model_dump()
            user_dict["phones"] = await uow.phones.find_all(PhoneInfoSchema, userId=user.id)
            user_dict["emails"] = await uow.emails.find_all(EmailInfoSchema, userId=user.id)
        return UserFullSchema.model_validate(user_dict)

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
            await uow.users.update_one(user_id, user_data.model_dump(), id=user_id)
            await uow.commit()
        self.logger.info(f"User with id: {user_id} updated")
        return True

    async def patch_user(self, user_id: int, user_data: UserOptionalSchema, uow: IUnitOfWork) -> bool:
        user_dict = user_data.model_dump(exclude_unset=True)
        self.logger.info(f"Patching user {user_id} with new data: {user_dict}")
        if not user_dict or all(value is None for value in user_dict.values()):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found fields for patch")
        async with uow:
            await uow.users.update_one(user_id, user_dict, id=user_id)
            await uow.commit()
        self.logger.info(f"User with id: {user_id} patched")
        return True

    async def delete_user(self, user_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Deleting user with id: {user_id}")
        async with uow:
            await uow.users.delete_one(user_id)
            await uow.commit()
        self.logger.info(f"User with id: {user_id} deleted")
        return True
