from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Employee Management System"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "A full-stack Employee Management System API built with FastAPI."
    )
    DEBUG: bool = True
    
    API_PREFIX: str = "/api/v1"
    
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
