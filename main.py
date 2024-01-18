from os import getenv

import uvicorn
from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
)

print(f"postgresql+asyncpg://"
      f"{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@"
      f"{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}")

print(f"postgresql+asyncpg://"
      f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
      f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
