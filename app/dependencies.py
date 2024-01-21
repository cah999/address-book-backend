from typing import Annotated

from fastapi import Depends

from exceptions.notfound import UserNotFound, EmailNotFound, PhoneNotFound
from services.emails import EmailsService
from services.phones import PhonesService
from services.users import UsersService
from utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDependency = Annotated[IUnitOfWork, Depends(UnitOfWork)]


async def validate_user(user_id: int, uow: UOWDependency):
    user = await UsersService().get_user(user_id, uow)
    if user is None:
        raise UserNotFound(user_id)
    return user


async def validate_email(email_id: int, uow: UOWDependency):
    email = await EmailsService().get_email(email_id, uow)
    if email is None:
        raise EmailNotFound(email_id)
    return email


async def validate_phone(phone_id: int, uow: UOWDependency):
    phone = await PhonesService().get_phone(phone_id, uow)
    if phone is None:
        raise PhoneNotFound(phone_id)
    return phone
