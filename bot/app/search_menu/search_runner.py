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
    Возвращает список username.
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
        # Backend сейчас возвращает:
        # {
        #     "results": [...]
        # }
        usernames = result.get(
            "results",
            result.get(
                "usernames",
                []
            )
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
    return list(
        dict.fromkeys(
            normalized
        )
    )
