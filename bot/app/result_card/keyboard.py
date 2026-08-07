from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def result_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⭐ Сохранить",
                    callback_data="save_username"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔄 Похожие",
                    callback_data="similar_username"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📊 Анализ",
                    callback_data="analyze_username"
                )
            ]

        ]
    )
