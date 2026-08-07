from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.search_menu.keyboards import (
    search_modes,
    number_mode
)

from app.search_menu.states import SearchMenuState


router = Router()



@router.message(
    lambda m:
    m.text == "🔎 Поиск"
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
    lambda c:
    c.data in [
        "search_5",
        "search_6"
    ]
)
async def choose_length(
    callback: CallbackQuery,
    state: FSMContext
):

    length = (
        "5"
        if callback.data == "search_5"
        else "6"
    )


    await state.update_data(
        length=length
    )


    await callback.message.answer(
        "Выберите тип username:",
        reply_markup=number_mode()
    )


    await callback.answer()



@router.callback_query(
    lambda c:
    c.data == "search_dictionary"
)
async def dictionary_start(
    callback: CallbackQuery,
    state: FSMContext
):

    await state.set_state(
        SearchMenuState.waiting_dictionary_word
    )


    await callback.message.answer(
        "📖 Введите слово для словаря:"
    )


    await callback.answer()
