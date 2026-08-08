from typing import Dict, Any, List
from app.search_menu.checker_client import (
    check_username
)
async def run_check(
    usernames: List[str]
) -> List[Dict[str, Any]]:
    """
    Проверяет список username через backend.
    Backend выполняет:
    - Telegram checker
    - Fragment checker
    - t.me checker
    Бот не импортирует backend-код напрямую.
    """
    if not usernames:
        return []
    results = []
    for username in usernames:
        username = str(
            username
        ).strip().lstrip("@")
        if not username:
            continue
        try:
            result = await check_username(
                username
            )
            if result:
                results.append(
                    result
                )
        except Exception as exc:
            results.append(
                {
                    "username": username,
                    "available": False,
                    "telegram": {
                        "taken": True,
                        "error": str(exc)
                    },
                    "fragment": {
                        "collectible": False,
                        "price": None
                    },
                    "tme": {
                        "available": False
                    },
                    "error": str(exc)
                }
            )
    return results
