import logging
import os
from typing import Dict, Any, List
import aiohttp
logger = logging.getLogger(__name__)
# ============================================================
# BACKEND
# ============================================================
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")
# ============================================================
# HTTP
# ============================================================
TIMEOUT = aiohttp.ClientTimeout(
    total=5
)
# ============================================================
# CHECK RUNNER
# ============================================================
async def run_check(
    usernames: List[str]
) -> List[Dict[str, Any]]:
    """
    Проверяет список username через BACKEND.
    Backend сам выполняет:
    - Telegram checker
    - Fragment checker
    - t.me checker
    Бот не дублирует checker-логику.
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
                    if response.status != 200:
                        logger.error(
                            "Checker HTTP %s for @%s",
                            response.status,
                            username
                        )
                        continue
                    result = await response.json()
                    if result:
                        results.append(
                            result
                        )
            except asyncio.TimeoutError:
                logger.error(
                    "Checker timeout for @%s",
                    username
                )
            except aiohttp.ClientError as exc:
                logger.error(
                    "Checker connection error for @%s: %s",
                    username,
                    exc
                )
            except Exception as exc:
                logger.exception(
                    "Checker error for @%s: %s",
                    username,
                    exc
                )
    return results
