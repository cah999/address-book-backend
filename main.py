from os import getenv

import uvicorn
from fastapi import FastAPI

from app.settings import settings
from api.users import router as users_router
from api.phones import router as phones_router
from api.emails import router as emails_router

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
)

routers = [users_router, phones_router, emails_router]

for router in routers:
    app.include_router(router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
