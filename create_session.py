import asyncio
import os
from telethon import TelegramClient

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

client = TelegramClient("teyzus_checker", API_ID, API_HASH)


async def main():
    await client.start()

    me = await client.get_me()

    print("================================")
    print("TELEGRAM SESSION CREATED")
    print("ID:", me.id)
    print("USERNAME:", me.username)
    print("SESSION FILE: teyzus_checker.session")
    print("================================")

    await client.disconnect()


asyncio.run(main())
