from app.search_menu.generator_client import (
    generate_usernames
)


async def run_search(
    length: int,
    numbers: bool
):

    result = await generate_usernames(
        length,
        numbers
    )


    usernames = result.get(
        "results",
        []
    )


    return usernames
