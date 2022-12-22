# Python
import os
from pathlib import Path

# Dotenv
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings():
    PROJECT_NAME: str = "sk-cleanup-orders"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", default="orders_db")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()