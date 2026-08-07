import asyncio

from app.search_loading.messages import (
    START_SEARCH,
    CHECKING_STEPS
)


async def run_search_animation(
    message,
    username
):

    progress = [
        "▱▱▱▱▱ 0%",
        "▰▱▱▱▱ 25%",
        "▰▰▱▱▱ 50%",
        "▰▰▰▱▱ 75%",
        "▰▰▰▰▰ 100%"
    ]


    for value in progress:

        await message.edit_text(
            START_SEARCH.format(
                username=username,
                progress=value
            )
        )

        await asyncio.sleep(1)



async def show_check_step(
    message,
    username,
    step
):

    await message.edit_text(
        f"""
🚀 TEYZUS AI

Проверяю:
@{username}

{step}

Прогресс:
▰▰▰▱▱ 60%
"""
    )
