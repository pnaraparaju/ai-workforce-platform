import os


class Settings:
    app_name: str = "AI Workforce Platform"
    environment: str = os.getenv("APP_ENV", "development")


settings = Settings()