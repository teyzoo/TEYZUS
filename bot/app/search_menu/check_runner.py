import asyncio
from typing import Dict, Any, List

from app.search_menu.checker_client import (
    check_username
)


async def _check_one(
    username: str
) -> Dict[str, Any] | None:

    username = (
        str(username)
        .strip()
        .lstrip("@")
    )

    if not username:
        return None

    try:

        result = await check_username(
            username
        )

        if not result:
            return None

        return result

    except Exception as exc:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "error": str(exc)
        }


async def run_check(
    usernames: List[str]
) -> List[Dict[str, Any]]:

    if not usernames:
        return []

    normalized = []

    for username in usernames:

        username = (
            str(username)
            .strip()
            .lstrip("@")
        )

        if username:
            normalized.append(
                username
            )

    normalized = list(
        dict.fromkeys(
            normalized
        )
    )

    results = await asyncio.gather(
        *[
            _check_one(username)
            for username in normalized
        ],
        return_exceptions=False
    )

    return [
        result
        for result in results
        if result is not None
    ]
