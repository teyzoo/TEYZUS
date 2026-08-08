from typing import Dict, Any, List
import os
import aiohttp
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")
TIMEOUT = aiohttp.ClientTimeout(total=20)
async def run_check(
    usernames: List[str]
) -> List[Dict[str, Any]]:
    """
    Проверяет список username через BACKEND.
    ВАЖНО:
    Бот не импортирует backend/app/checker напрямую.
    Проверка выполняется через HTTP API:
        POST /checker/
    """
    if not usernames:
        return []
    results = []
    async with aiohttp.ClientSession(
        timeout=TIMEOUT
    ) as session:
        for username in usernames:
            username = str(
                username
            ).strip().lstrip("@")
            if not username:
                continue
            try:
                async with session.post(
                    f"{BACKEND_URL}/checker/",
                    json={
                        "username": username
                    }
                ) as response:
                    if response.status >= 400:
                        results.append({
                            "username": username,
                            "available": False,
                            "error": (
                                f"Backend HTTP "
                                f"{response.status}"
                            )
                        })
                        continue
                    data = await response.json()
                    if isinstance(data, dict):
                        results.append(data)
            except Exception as exc:
                results.append({
                    "username": username,
                    "available": False,
                    "error": str(exc)
                })
    return results
