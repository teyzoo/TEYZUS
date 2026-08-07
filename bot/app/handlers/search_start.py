from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.search import SearchState


router = Router()


@router.message(
    lambda message:
    message.text == "🔎 Поиск"
)
async def start_search(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        SearchState.waiting_username
    )

    await message.answer(
        "🔎 Отправьте username для поиска\n\n"
        "Пример:\n"
        "@future"
    )
