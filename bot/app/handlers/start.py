from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.api.client import create_user
from app.keyboards.main import main_menu
router = Router()
@router.message(CommandStart())
async def start_handler(
    message: Message
):
    """
    Обработка /start.
    Регистрация пользователя в backend
    не должна ломать ответ Telegram-бота.
    """
    user = message.from_user
    user_data = {
        "telegram_id": str(user.id),
        "username": user.username,
        "first_name": user.first_name,
        "language": user.language_code,
    }
    # Backend может быть временно недоступен.
    # Это НЕ должно мешать /start.
    try:
        await create_user(
            user_data
        )
    except Exception:
        pass
    await message.answer(
        "🚀 Добро пожаловать в TEYZUS!\n\n"
        "Здесь ты можешь найти интересные Telegram username, "
        "проверить их доступность и в дальнейшем работать с ними "
        "через Marketplace.\n\n"
        "Выбери нужный раздел ниже 👇",
        reply_markup=main_menu(),
    )
