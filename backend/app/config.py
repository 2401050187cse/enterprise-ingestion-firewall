import os
from pydantic_settings import BaseSettings

# Dynamically resolve the absolute path of the root project folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ENV_PATH = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    class Config:
        env_file = ENV_PATH
        extra = "ignore"

settings = Settings()