from typing import Dict, Any, List, Callable, Awaitable
from app.checker.service import check_username
async def run_check(
    usernames: List[str],
    progress_callback: Callable[
        [str, int, int],
        Awaitable[None]
    ] | None = None
) -> List[Dict[str, Any]]:
    """
    Проверяет список username по одному.
    progress_callback получает:
        username
        current
        total
    Это позволяет показывать пользователю,
    какой именно username сейчас проверяется.
    """
    if not usernames:
        return []
    results = []
    total = len(usernames)
    for index, username in enumerate(
        usernames,
        start=1
    ):
        username = (
            str(username)
            .strip()
            .lstrip("@")
        )
        if not username:
            continue
        if progress_callback:
            await progress_callback(
                username,
                index,
                total
            )
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
                    "checked": False,
                    "telegram": {
                        "taken": None,
                        "checked": False
                    },
                    "fragment": {
                        "collectible": None,
                        "price": None,
                        "checked": False
                    },
                    "tme": {
                        "available": None,
                        "checked": False
                    },
                    "error": str(exc)
                }
            )
    return results
