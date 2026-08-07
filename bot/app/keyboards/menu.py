from aiogram import Router
from aiogram.types import Message

from app.keyboards.main import main_menu


router = Router()


@router.message()
async def menu_handler(
    message: Message
):

    text = message.text


    if text == "🔎 Поиск":

        await message.answer(
            "🔎 Введите username для поиска:"
        )


    elif text == "💎 Premium":

        await message.answer(
            "💎 TEYZUS Premium\n\n"
            "♾️ Безлимитный поиск\n"
            "🚨 Ловушки\n"
            "📊 Расширенный AI анализ"
        )


    elif text == "👤 Профиль":

        await message.answer(
            "👤 Профиль пользователя"
        )


    elif text == "👥 Рефералы":

        await message.answer(
            "👥 Ваша реферальная система"
        )


    elif text == "🏪 Marketplace":

        await message.answer(
            "🏪 Marketplace скоро будет доступен"
        )


    elif text == "💬 Поддержка":

        await message.answer(
            "💬 Поддержка TEYZUS"
        )
