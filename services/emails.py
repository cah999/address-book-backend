import logging

from fastapi import HTTPException, status

from schemas.emails import EmailAddSchema, EmailOptionalSchema, EmailSchema
from schemas.users import UserSchema, UserInfoSchema
from utils.unitofwork import IUnitOfWork


class EmailsService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def get_user_emails(self, user_id: int, uow: IUnitOfWork) -> list[EmailSchema]:
        async with uow:
            user = await uow.users.find_one(user_id, schema=UserInfoSchema)
            if user is None:
                self.logger.info(f"User with id: {user_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
            emails = await uow.emails.find_all(schema=EmailSchema, userId=user_id)
        return [EmailSchema.model_validate(email) for email in emails]

    async def add_email(self, user_id: int, email_data: EmailAddSchema, uow: IUnitOfWork) -> int:
        self.logger.info(f"Adding email for user with id: {user_id}")
        email_dict = email_data.model_dump()
        email_dict["userId"] = user_id
        async with uow:
            user = await uow.users.find_one(user_id, schema=UserInfoSchema)
            if user is None:
                self.logger.info(f"User with id: {user_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id = {user_id} not found")
            email_id = await uow.emails.add_one(email_dict)
            await uow.commit()
        self.logger.info(f"Email added for user with id: {user_id}")
        return int(email_id)

    async def update_email(self, email_id: int, email_data: EmailAddSchema, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Updating email with id: {email_id} with data: {email_data}")
        async with uow:
            await uow.emails.update_one(email_id, email_data.model_dump(), id=email_id)
            await uow.commit()
        self.logger.info(f"Email with id: {email_id} updated")
        return True

    async def patch_email(self, email_id: int, email_data: EmailOptionalSchema, uow: IUnitOfWork) -> bool:
        email_dict = email_data.model_dump(exclude_unset=True)
        self.logger.info(f"Patching email with id: {email_id} with data: {email_dict}")
        if all(value is None for value in email_dict.values()) or len(email_dict) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found fields for update")
        async with uow:
            await uow.emails.update_one(email_id, email_dict, id=email_id)
            await uow.commit()
        self.logger.info(f"Email with id: {email_id} patched")
        return True

    async def delete_email(self, email_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Deleting email with id: {email_id}")
        async with uow:
            res = await uow.emails.delete_one(email_id)
            if res is None:
                self.logger.info(f"Email with id: {email_id} not found")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Email with id = {email_id} not found")
            await uow.commit()
        self.logger.info(f"Email with id: {email_id} deleted")
        return True
