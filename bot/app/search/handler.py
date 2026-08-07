from aiogram import Router
from aiogram.types import Message

from app.search.client import search_username


router = Router()


@router.message()
async def search_handler(
    message: Message
):

    if not message.text:
        return


    if message.text.startswith("/"):
        return


    result = await search_username(
        str(message.from_user.id),
        message.text
    )


    text = "🔎 TEYZUS Search\n\n"


    text += (
        f"Запрос: @{result.get('normalized_query')}\n\n"
    )


    for item in result.get(
        "results",
        []
    ):

        text += (
            f"@{item['username']}\n"
            f"Статус: {item['status']}\n\n"
        )


    await message.answer(
        text
    )
