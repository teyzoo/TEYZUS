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
    user_data = {
        "telegram_id": str(
            message.from_user.id
        ),
        "username": (
            message.from_user.username
        ),
        "first_name": (
            message.from_user.first_name
        ),
        "language": (
            message.from_user.language_code
        )
    }
    # Ошибка backend не должна
    # ломать приветствие бота.
    await create_user(
        user_data
    )
    await message.answer(
        "🚀 Добро пожаловать в TEYZUS!\n\n"
        "Здесь ты можешь находить "
        "интересные Telegram username, "
        "проверять их доступность и "
        "оценивать найденные варианты.\n\n"
        "🏪 В Marketplace можно будет "
        "найти и продать username.\n\n"
        "Выбери нужный раздел ниже:",
        reply_markup=main_menu()
    )
