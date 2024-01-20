from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.dependencies import UOWDependency
from schemas.emails import EmailAddSchema, EmailOptionalSchema
from services.emails import EmailsService

router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.get("/{user_id}")
async def get_user_emails(user_id: int, session: UOWDependency):
    return await EmailsService().get_user_emails(user_id, session)


@router.post("/{user_id}/new")
async def add_email(user_id: int, email_data: EmailAddSchema, session: UOWDependency):
    return await EmailsService().add_email(user_id, email_data, session)


@router.put("/{email_id}")
async def update_email(email_id: int, email_data: EmailAddSchema, session: UOWDependency):
    await EmailsService().update_email(email_id, email_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully updated"})


@router.patch("/{email_id}")
async def patch_email(email_id: int, email_data: EmailOptionalSchema, session: UOWDependency):
    await EmailsService().patch_email(email_id, email_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully patched"})


@router.delete("/{email_id}")
async def delete_email(email_id: int, session: UOWDependency):
    await EmailsService().delete_email(email_id, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully deleted"})
