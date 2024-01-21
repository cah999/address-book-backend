from fastapi import HTTPException


class UserNotFound(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"User with id={user_id} not found")


class EmailNotFound(HTTPException):
    def __init__(self, email_id: int):
        super().__init__(status_code=404, detail=f"Email with id={email_id} not found")


class PhoneNotFound(HTTPException):
    def __init__(self, phone_id: int):
        super().__init__(status_code=404, detail=f"Phone with id={phone_id} not found")
