from aiogram import Router
from aiogram.types import Message

from app.api.client import create_user
from app.keyboards.main import main_menu


router = Router()


@router.message()
async def start_handler(message: Message):
    user_data = {
        "telegram_id": str(message.from_user.id),
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "language": message.from_user.language_code,
    }

    try:
        await create_user(user_data)
    except Exception as e:
        print(f"USER CREATE ERROR: {e}")

    await message.answer(
        "🚀 Добро пожаловать в TEYZUS\n\n"
        "Здесь ты можешь:\n"
        "🔎 находить свободные Telegram username\n"
        "💎 проверять редкие и ценные username\n"
        "🏪 находить и продавать username через Marketplace\n\n"
        "Выбери нужный раздел ниже:",
        reply_markup=main_menu(),
    )
