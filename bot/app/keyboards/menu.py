from aiogram import Router
from aiogram.types import CallbackQuery
from app.search_menu.keyboards import search_modes
router = Router()
@router.callback_query(
    lambda c: c.data == "menu_search"
)
async def menu_search(
    callback: CallbackQuery
):
    await callback.message.edit_text(
        "🔎 TEYZUS Search\n\n"
        "Выберите режим:",
        reply_markup=search_modes()
    )
    await callback.answer()
@router.callback_query(
    lambda c: c.data == "menu_premium"
)
async def menu_premium(
    callback: CallbackQuery
):
    await callback.message.answer(
        "💎 TEYZUS Premium\n\n"
        "♾️ Безлимитный поиск\n"
        "🚨 Ловушки\n"
        "📊 Расширенный анализ"
    )
    await callback.answer()
@router.callback_query(
    lambda c: c.data == "menu_profile"
)
async def menu_profile(
    callback: CallbackQuery
):
    await callback.message.answer(
        "👤 Профиль пользователя"
    )
    await callback.answer()
@router.callback_query(
    lambda c: c.data == "menu_referrals"
)
async def menu_referrals(
    callback: CallbackQuery
):
    await callback.message.answer(
        "👥 Ваша реферальная система"
    )
    await callback.answer()
@router.callback_query(
    lambda c: c.data == "menu_marketplace"
)
async def menu_marketplace(
    callback: CallbackQuery
):
    await callback.message.answer(
        "🏪 Marketplace\n\n"
        "Здесь можно будет находить "
        "и продавать Telegram username."
    )
    await callback.answer()
@router.callback_query(
    lambda c: c.data == "menu_support"
)
async def menu_support(
    callback: CallbackQuery
):
    await callback.message.answer(
        "💬 Поддержка TEYZUS"
    )
    await callback.answer()
