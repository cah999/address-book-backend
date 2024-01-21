from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.dependencies import UOWDependency, validate_user, validate_phone
from schemas.phones import PhoneAddSchema, PhoneOptionalSchema, PhoneSchema
from schemas.users import UserFullSchema
from services.phones import PhonesService

router = APIRouter(
    prefix="/phones",
    tags=["Phones"],
)


@router.get("/{user_id}")
async def get_user_phones(user: Annotated[UserFullSchema, Depends(validate_user)], uow: UOWDependency):
    return await PhonesService().get_user_phones(user.id, uow)


@router.post("/{user_id}/new")
async def add_phone(user: Annotated[UserFullSchema, Depends(validate_user)], phone_data: PhoneAddSchema,
                    uow: UOWDependency):
    return await PhonesService().add_phone(user.id, phone_data, uow)


@router.put("/{phone_id}")
async def update_phone(phone: Annotated[PhoneSchema, Depends(validate_phone)], phone_data: PhoneAddSchema,
                       uow: UOWDependency):
    await PhonesService().update_phone(phone.id, phone_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully updated"})


@router.patch("/{phone_id}")
async def patch_phone(phone: Annotated[PhoneSchema, Depends(validate_phone)], phone_data: PhoneOptionalSchema,
                      uow: UOWDependency):
    await PhonesService().patch_phone(phone.id, phone_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully patched"})


@router.delete("/{phone_id}")
async def delete_phone(phone: Annotated[PhoneSchema, Depends(validate_phone)], uow: UOWDependency):
    await PhonesService().delete_phone(phone.id, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully deleted"})
