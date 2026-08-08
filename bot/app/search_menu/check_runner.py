import asyncio
from typing import Dict, Any, List
import aiohttp
from app.search_menu.checker_client import check_username
# Максимальное количество одновременно выполняемых проверок.
# Начни с 100–200 на Render.
# Если всё стабильно — можно поднимать.
CONCURRENCY = 200
async def _check_one(
    username: str,
    semaphore: asyncio.Semaphore
) -> Dict[str, Any] | None:
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )
    if not username:
        return None
    async with semaphore:
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
    # Убираем дубли.
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
    if not normalized:
        return []
    semaphore = asyncio.Semaphore(
        CONCURRENCY
    )
    tasks = [
        asyncio.create_task(
            _check_one(
                username,
                semaphore
            )
        )
        for username in normalized
    ]
    results = await asyncio.gather(
        *tasks,
        return_exceptions=False
    )
    return [
        result
        for result in results
        if result is not None
    ]
