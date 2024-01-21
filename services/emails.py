import logging

from fastapi import HTTPException, status

from schemas.emails import EmailAddSchema, EmailOptionalSchema, EmailSchema
from utils.unitofwork import IUnitOfWork


class EmailsService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    async def get_email(email_id: int, uow: IUnitOfWork) -> EmailSchema:
        async with uow:
            email = await uow.emails.find_one(email_id, schema=EmailSchema)
        return email

    async def get_user_emails(self, user_id: int, uow: IUnitOfWork) -> list[EmailSchema]:
        self.logger.info(f"Getting emails for user with id: {user_id}")
        async with uow:
            emails = await uow.emails.find_all(schema=EmailSchema, userId=user_id)
        return [EmailSchema.model_validate(email) for email in emails]

    async def add_email(self, user_id: int, email_data: EmailAddSchema, uow: IUnitOfWork) -> int:
        self.logger.info(f"Adding email for user with id: {user_id}")
        email_dict = email_data.model_dump()
        email_dict["userId"] = user_id
        async with uow:
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
        if not email_dict or all(value is None for value in email_dict.values()):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found fields for update")
        async with uow:
            await uow.emails.update_one(email_id, email_dict, id=email_id)
            await uow.commit()
        self.logger.info(f"Email with id: {email_id} patched")
        return True

    async def delete_email(self, email_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Deleting email with id: {email_id}")
        async with uow:
            await uow.emails.delete_one(email_id)
            await uow.commit()
        self.logger.info(f"Email with id: {email_id} deleted")
        return True
