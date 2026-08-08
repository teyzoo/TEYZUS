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
    Backend возвращает:
        {
            "results": [...]
        }
    Возвращаем:
        [
            "username1",
            "username2",
            ...
        ]
    """
    result = await generate_usernames(
        length=length,
        numbers=numbers
    )
    if not result:
        return []
    if isinstance(result, list):
        usernames = result
    elif isinstance(result, dict):
        usernames = result.get(
            "results",
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
