from aiogram import Router
from aiogram.types import Message

from app.api.client import create_user


router = Router()


@router.message()
async def start_handler(message: Message):

    user_data = {
        "telegram_id": str(message.from_user.id),
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "language": message.from_user.language_code
    }


    await create_user(
        user_data
    )


    await message.answer(
        "🚀 Добро пожаловать в TEYZUS\n\n"
        "AI-платформа для поиска и оценки Telegram username."
    )
