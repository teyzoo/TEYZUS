from typing import List, Dict, Any

from app.checker.service import check_username


async def run_check(
    usernames: List[str]
) -> List[Dict[str, Any]]:
    """
    Проверяет список username.

    Для каждого username запускаются:

    - Telegram checker
    - Fragment checker
    - t.me checker

    Возвращается список результатов.

    Никакие результаты не подменяются
    статическими значениями.
    """

    if not usernames:
        return []

    results = []

    for username in usernames:

        username = username.strip().lstrip("@")

        if not username:
            continue

        try:
            result = await check_username(
                username
            )

            results.append(
                result
            )

        except Exception as e:

            print(
                f"CHECK ERROR @{username}: {e}"
            )

            results.append(
                {
                    "username": username,
                    "telegram": {
                        "taken": None,
                        "error": str(e)
                    },
                    "fragment": {
                        "collectible": None,
                        "price": None,
                        "error": str(e)
                    },
                    "tme": {
                        "available": None,
                        "error": str(e)
                    },
                    "available": False,
                    "error": str(e)
                }
            )

    return results
