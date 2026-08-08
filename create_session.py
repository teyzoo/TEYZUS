import asyncio
import os

from telethon import TelegramClient


API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]


async def main():
    client = TelegramClient(
        "teyzus_checker",
        API_ID,
        API_HASH
    )

    await client.connect()

    print("TELETHON CONNECTED")
    print("Authorized:", await client.is_user_authorized())

    await client.disconnect()


asyncio.run(main())
