from typing import List
from app.search_menu.generator_client import (
    generate_usernames
)
async def run_search(
    length: int,
    numbers: bool
) -> List[str]:
    """
    Запускает генерацию username через backend.
    Возвращает список username для дальнейшей проверки.
    """
    result = await generate_usernames(
        length=length,
        numbers=numbers
    )
    if not result:
        return []
    # Backend может вернуть непосредственно список:
    #
    # [
    #     "username1",
    #     "username2"
    # ]
    #
    if isinstance(result, list):
        usernames = result
    # Или объект:
    #
    # {
    #     "usernames": [...]
    # }
    #
    elif isinstance(result, dict):
        usernames = result.get(
            "usernames",
            []
        )
    else:
        return []
    normalized = []
    for username in usernames:
        if not username:
            continue
        username = str(
            username
        ).strip().lstrip("@")
        if username:
            normalized.append(
                username
            )
    return normalized
