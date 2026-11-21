from pathlib import Path

from pydantic_settings import BaseSettings


ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_ip: str
    db_port: str
    db_name: str

    class Config:
        env_file = ENV_FILE

settings = Settings()