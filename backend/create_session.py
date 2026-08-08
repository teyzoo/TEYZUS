import asyncio
import os

from telethon import TelegramClient


API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

SESSION_NAME = "teyzus_checker"


async def main():
    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH
    )

    await client.start()

    me = await client.get_me()

    print(
        f"SESSION CREATED FOR: "
        f"@{me.username or me.id}"
    )

    print(
        "Session file:",
        f"{SESSION_NAME}.session"
    )

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
