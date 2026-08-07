import os


class Settings:
    BOT_TOKEN = os.getenv(
        "BOT_TOKEN",
        ""
    )


settings = Settings()
