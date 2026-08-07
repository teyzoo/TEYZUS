from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.search_menu.keyboards import (
    search_modes,
    number_mode
)

from app.search_loading.animation import (
    run_search_animation
)

from app.search_menu.search_runner import (
    run_search
)

from app.search_menu.check_runner import (
    run_check
)


router = Router()



@router.message(
    lambda m: m.text == "🔎 Поиск"
)
async def open_search(
    message: Message
):

    await message.answer(
        "🔎 TEYZUS Search\n\n"
        "Выберите режим:",
        reply_markup=search_modes()
    )



@router.callback_query(
    lambda c: c.data in [
        "search_5",
        "search_6"
    ]
)
async def choose_length(
    callback: CallbackQuery,
    state: FSMContext
):

    length = 5

    if callback.data == "search_6":
        length = 6


    await state.update_data(
        length=length
    )


    await callback.message.answer(
        "Выберите тип username:",
        reply_markup=number_mode()
    )


    await callback.answer()



@router.callback_query(
    lambda c: c.data in [
        "letters_only",
        "with_numbers"
    ]
)
async def start_generation(
    callback: CallbackQuery,
    state: FSMContext
):

    data = await state.get_data()


    length = data.get(
        "length",
        5
    )


    numbers = (
        callback.data == "with_numbers"
    )


    await callback.answer()


    loading = await callback.message.answer(
        "🚀 TEYZUS AI\n\n"
        "🔎 Ищу юзернейм..."
    )


    await run_search_animation(
        loading,
        "username"
    )


    usernames = await run_search(
        length,
        numbers
    )


    if not usernames:

        await loading.edit_text(
            "❌ Ничего не найдено"
        )

        await state.clear()

        return



    await loading.edit_text(
        "🔍 Проверяю найденные username...\n\n"
        "Telegram + Fragment + t.me"
    )


    checked = await run_check(
        usernames
    )


    text = (
        "🚀 TEYZUS AI\n\n"
        "✅ Результаты:\n\n"
    )


    for item in checked[:10]:

        username = item.get(
            "username"
        )

        status = (
            "⚡ Свободен"
            if item.get("available")
            else "❌ Занят"
        )


        text += (
            f"@{username}\n"
            f"{status}\n\n"
        )


    await loading.edit_text(
        text
    )


    await state.clear()
