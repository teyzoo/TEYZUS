from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def search_modes():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1️⃣ 5 букв",
                    callback_data="search_5"
                )
            ],
            [
                InlineKeyboardButton(
                    text="2️⃣ 6 букв",
                    callback_data="search_6"
                )
            ],
            [
                InlineKeyboardButton(
                    text="3️⃣ 🚨 Ловушка",
                    callback_data="search_trap"
                )
            ],
            [
                InlineKeyboardButton(
                    text="4️⃣ ⚙️ Фильтры",
                    callback_data="search_filters"
                )
            ],
            [
                InlineKeyboardButton(
                    text="5️⃣ 📖 Словарь",
                    callback_data="search_dictionary"
                )
            ]
        ]
    )



def number_mode():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔤 Только буквы",
                    callback_data="letters_only"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔢 С цифрами",
                    callback_data="with_numbers"
                )
            ]
        ]
    )
