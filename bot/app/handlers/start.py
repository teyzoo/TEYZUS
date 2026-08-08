import logging
from aiogram import Router
from aiogram.types import Message
from app.api.client import create_user
router = Router()
logger = logging.getLogger(__name__)
@router.message()
async def start_handler(message: Message):
    user_data = {
        "telegram_id": str(message.from_user.id),
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "language": message.from_user.language_code,
    }
    # Регистрация пользователя не должна блокировать ответ бота.
    try:
        await create_user(
            user_data
        )
    except Exception:
        logger.exception(
            "Failed to create user: telegram_id=%s",
            message.from_user.id,
        )
    await message.answer(
        "🚀 Добро пожаловать в TEYZUS\n\n"
        "AI-платформа для поиска и оценки Telegram username."
    )
