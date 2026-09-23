from app.config import settings
from app.greetings import say_hello


if __name__ == "__main__":
    print(say_hello("Praneeth"))
    print(f"Application: {settings.app_name}")
    print(f"Environment: {settings.environment}")