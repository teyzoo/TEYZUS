import asyncio
from typing import Any, Dict, List
from app.search_menu.checker_client import (
    check_username
)
MAX_CONCURRENT_CHECKS = 100
async def _check_one(
    username: str
) -> Dict[str, Any] | None:
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
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
    normalized = list(
        dict.fromkeys(
            str(username)
            .strip()
            .lstrip("@")
            .lower()
            for username in usernames
            if username
        )
    )
    semaphore = asyncio.Semaphore(
        MAX_CONCURRENT_CHECKS
    )
    async def limited_check(
        username: str
    ):
        async with semaphore:
            return await _check_one(
                username
            )
    results = await asyncio.gather(
        *[
            limited_check(username)
            for username in normalized
        ],
        return_exceptions=False
    )
    return [
        result
        for result in results
        if result is not None
    ]
