from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from app.dependencies import UOWDependency, validate_user, validate_email
from schemas.emails import EmailAddSchema, EmailOptionalSchema, EmailSchema
from schemas.users import UserFullSchema
from services.emails import EmailsService

router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.get("/{user_id}")
async def get_user_emails(user: Annotated[UserFullSchema, Depends(validate_user)], session: UOWDependency):
    return await EmailsService().get_user_emails(user.id, session)


@router.post("/{user_id}/new")
async def add_email(user: Annotated[UserFullSchema, Depends(validate_user)], email_data: EmailAddSchema,
                    session: UOWDependency):
    return await EmailsService().add_email(user.id, email_data, session)


@router.put("/{email_id}")
async def update_email(email: Annotated[EmailSchema, Depends(validate_email)], email_data: EmailAddSchema,
                       session: UOWDependency):
    await EmailsService().update_email(email.id, email_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully updated"})


@router.patch("/{email_id}")
async def patch_email(email: Annotated[EmailSchema, Depends(validate_email)], email_data: EmailOptionalSchema,
                      session: UOWDependency):
    await EmailsService().patch_email(email.id, email_data, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully patched"})


@router.delete("/{email_id}")
async def delete_email(email: Annotated[EmailSchema, Depends(validate_email)], session: UOWDependency):
    await EmailsService().delete_email(email.id, session)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Email successfully deleted"})
