import logging
from aiogram import Router
from aiogram.types import Message
from app.api.client import create_user
from app.keyboards.main import main_menu
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
    # ========================================================
    # USER REGISTRATION
    # ========================================================
    #
    # Ошибка backend не должна блокировать Telegram-ответ.
    #
    try:
        await create_user(
            user_data
        )
    except Exception:
        logger.exception(
            "Failed to create user: telegram_id=%s",
            message.from_user.id,
        )
    # ========================================================
    # MAIN MENU
    # ========================================================
    await message.answer(
    "🚀 Добро пожаловать в TEYZUS!\n\n"
    "Здесь ты можешь найти подходящий Telegram username, "
    "проверить его доступность и оценить его стоимость.\n\n"
    "🔎 Ищи редкие и интересные юзернеймы\n"
    "💎 Оценивай их потенциал и стоимость\n"
    "🏪 Покупай и продавай username в Marketplace\n"
    "📊 Следи за своими находками и результатами\n\n"
    "Выбирай нужный раздел в меню ниже 👇",
    reply_markup=main_menu(),
)
