from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.search import SearchState
from app.search.client import search_username


router = Router()


@router.message(
    SearchState.waiting_username
)
async def process_search(
    message: Message,
    state: FSMContext
):

    await state.clear()


    result = await search_username(
        str(message.from_user.id),
        message.text
    )


    text = "🔎 TEYZUS AI Search\n\n"


    for item in result.get(
        "results",
        []
    ):

        text += (
            f"@{item['username']}\n"
            f"⏳ {item['status']}\n\n"
        )


    await message.answer(
        text
    )
