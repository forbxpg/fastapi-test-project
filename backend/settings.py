"""App settings."""

import os

from dotenv import load_dotenv
from email_validator.rfc_constants import EMAIL_MAX_LENGTH

load_dotenv()


DB_URL = os.environ.get(
    "DB_URL",
    "postgresql+asyncpg://postgres:password@localhost:5432/postgres",
)
DB_ECHO = os.environ.get("DB_ECHO", "False").lower() == "true"


# Constraints and constants
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128
