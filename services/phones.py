import logging

from fastapi import HTTPException, status

from schemas.phones import PhoneAddSchema, PhoneOptionalSchema, PhoneSchema
from utils.unitofwork import IUnitOfWork


class PhonesService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def get_phone(self, phone_id: int, uow: IUnitOfWork) -> PhoneSchema:
        self.logger.info(f"Getting phone with id: {phone_id}")
        async with uow:
            phone = await uow.phones.find_one(phone_id, schema=PhoneSchema)
        return phone

    async def get_user_phones(self, user_id: int, uow: IUnitOfWork) -> list[PhoneSchema]:
        self.logger.info(f"Getting phones for user with id: {user_id}")
        async with uow:
            phones = await uow.phones.find_all(schema=PhoneSchema, userId=user_id)
        self.logger.info(f"Phones for user with id: {user_id} successfully received")
        return [PhoneSchema.model_validate(phone) for phone in phones]

    async def add_phone(self, user_id: int, phone_data: PhoneAddSchema, uow: IUnitOfWork) -> int:
        phone_dict = phone_data.model_dump()
        phone_dict["userId"] = user_id
        self.logger.info(f"Adding phone for user with id: {user_id}")
        async with uow:
            phone_id = await uow.phones.add_one(phone_dict)
            await uow.commit()
        self.logger.info(f"Phone added for user with id: {user_id}")
        return int(phone_id)

    async def update_phone(self, phone_id: int, phone_data: PhoneAddSchema, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Updating phone with id: {phone_id} with data: {phone_data}")
        async with uow:
            await uow.phones.update_one(phone_id, phone_data.model_dump(), id=phone_id)
            await uow.commit()
        self.logger.info(f"Phone with id: {phone_id} updated")
        return True

    async def patch_phone(self, phone_id: int, phone_data: PhoneOptionalSchema, uow: IUnitOfWork) -> bool:
        phone_dict = phone_data.model_dump(exclude_unset=True)
        self.logger.info(f"Patching phone with id: {phone_id} with data: {phone_dict}")
        if all(value is None for value in phone_dict.values()) or len(phone_dict) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found fields for update")
        async with uow:
            await uow.phones.update_one(phone_id, phone_dict, id=phone_id)
            await uow.commit()
        self.logger.info(f"Phone with id: {phone_id} patched")
        return True

    async def delete_phone(self, phone_id: int, uow: IUnitOfWork) -> bool:
        self.logger.info(f"Deleting phone with id: {phone_id}")
        async with uow:
            await uow.phones.delete_one(phone_id)
            await uow.commit()
        self.logger.info(f"Phone with id: {phone_id} deleted")
        return True
