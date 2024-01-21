from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    API_NAME: str = "Address Book API"
    API_VERSION: str = "1.0.0b"
    API_PREFIX: str = "/api"

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str


load_dotenv()
settings = AppSettings()
