import os
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str = "openai/gpt-oss-120b"

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        extra="ignore"
    )


settings = Settings()