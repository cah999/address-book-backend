import uvicorn
from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
