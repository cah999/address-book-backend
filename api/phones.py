from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.dependencies import UOWDependency
from schemas.phones import PhoneAddSchema, PhoneOptionalSchema
from services.phones import PhonesService

router = APIRouter(
    prefix="/phones",
    tags=["Phones"],
)


@router.get("/{user_id}")
async def get_user_phones(user_id: int, uow: UOWDependency):
    return await PhonesService().get_user_phones(user_id, uow)


@router.post("/{user_id}/new")
async def add_phone(user_id: int, phone_data: PhoneAddSchema, uow: UOWDependency):
    return await PhonesService().add_phone(user_id, phone_data, uow)


@router.put("/{phone_id}")
async def update_phone(phone_id: int, phone_data: PhoneAddSchema, uow: UOWDependency):
    await PhonesService().update_phone(phone_id, phone_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully updated"})


@router.patch("/{phone_id}")
async def patch_phone(phone_id: int, phone_data: PhoneOptionalSchema, uow: UOWDependency):
    await PhonesService().patch_phone(phone_id, phone_data, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully patched"})


@router.delete("/{phone_id}")
async def delete_phone(phone_id: int, uow: UOWDependency):
    await PhonesService().delete_phone(phone_id, uow)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Phone successfully deleted"})
