import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name: str = "AI Workforce Platform"
    environment: str = os.getenv("APP_ENV", "development")


settings = Settings()