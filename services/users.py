from schemas.users import UserSchema
from utils.unitofwork import IUnitOfWork


class UsersService:
    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    async def add_user(self, uow: IUnitOfWork, user: UserSchema):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id
