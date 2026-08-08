from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Поиск",
                    callback_data="menu_search"
                ),
                InlineKeyboardButton(
                    text="💎 Premium",
                    callback_data="menu_premium"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 Профиль",
                    callback_data="menu_profile"
                ),
                InlineKeyboardButton(
                    text="👥 Рефералы",
                    callback_data="menu_referrals"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏪 Marketplace",
                    callback_data="menu_marketplace"
                ),
                InlineKeyboardButton(
                    text="💬 Поддержка",
                    callback_data="menu_support"
                )
            ]
        ]
    )
