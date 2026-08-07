import os


class Settings:
    APP_NAME = "TEYZUS API"
    VERSION = "0.1.0"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://localhost/teyzus"
    )


settings = Settings()
