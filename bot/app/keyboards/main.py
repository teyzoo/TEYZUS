from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🔎 Поиск"
                ),
                KeyboardButton(
                    text="💎 Premium"
                )
            ],
            [
                KeyboardButton(
                    text="👤 Профиль"
                ),
                KeyboardButton(
                    text="👥 Рефералы"
                )
            ],
            [
                KeyboardButton(
                    text="🏪 Marketplace"
                ),
                KeyboardButton(
                    text="💬 Поддержка"
                )
            ]
        ],
        resize_keyboard=True
    )
