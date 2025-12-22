import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")
    SESSION_COOKIE_NAME: str = os.getenv("SESSION_COOKIE_NAME", "adam8_session")
    PERMANENT_SESSION_LIFETIME: int = int(os.getenv("PERMANENT_SESSION_LIFETIME", 3600))

config = Config()