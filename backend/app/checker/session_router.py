import os
from fastapi import APIRouter
from telethon import TelegramClient
router = APIRouter(
    prefix="/telegram-session",
    tags=["Telegram Session"]
)
API_ID = int(
    os.environ["API_ID"]
)
API_HASH = os.environ["API_HASH"]
SESSION_NAME = "teyzus_checker"
client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH
)
@router.get("/status")
async def session_status():
    if not client.is_connected():
        await client.connect()
    authorized = await client.is_user_authorized()
    return {
        "authorized": authorized
    }
