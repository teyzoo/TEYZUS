import os
from dotenv import load_dotenv


load_dotenv()


class Settings:

    BOT_TOKEN = os.getenv(
        "BOT_TOKEN"
    )

    OWNER_ID = int(
        os.getenv(
            "OWNER_ID",
            "0"
        )
    )


settings = Settings()
