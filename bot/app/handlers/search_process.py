from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.search import SearchState
from app.search.client import search_username
from app.cards.builder import build_username_card


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


    results = result.get(
        "results",
        []
    )


    if not results:

        await message.answer(
            "❌ Username не найден"
        )

        return


    first = results[0]


    card = build_username_card(
        username=first.get(
            "username"
        ),
        ai=first.get(
            "ai_score"
        ),
        price_min=first.get(
            "estimated_price_min"
        ),
        price_max=first.get(
            "estimated_price_max"
        )
    )


    await message.answer(
        card
    )
