import asyncio
import logging
import os
import aiohttp
logger = logging.getLogger(__name__)
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")
REQUEST_TIMEOUT = aiohttp.ClientTimeout(
    total=30
)
async def check_username(
    username: str
):
    """
    Отправляет username в backend checker.
    Backend:
        POST /checker/
    Возвращает полный результат проверки.
    """
    username = str(
        username
    ).strip().lstrip("@")
    if not username:
        return None
    url = f"{BACKEND_URL}/checker/"
    data = {
        "username": username
    }
    try:
        async with aiohttp.ClientSession(
            timeout=REQUEST_TIMEOUT
        ) as session:
            async with session.post(
                url,
                json=data
            ) as response:
                try:
                    result = await response.json()
                except Exception:
                    text = await response.text()
                    logger.error(
                        "Backend checker returned non-JSON response: %s",
                        text
                    )
                    return None
                if response.status >= 400:
                    logger.error(
                        "Checker backend error %s: %s",
                        response.status,
                        result
                    )
                    return None
                return result
    except asyncio.TimeoutError:
        logger.exception(
            "Checker backend timeout: %s",
            url
        )
        return None
    except aiohttp.ClientError:
        logger.exception(
            "Checker backend connection error: %s",
            url
        )
        return None
    except Exception:
        logger.exception(
            "Unexpected checker error"
        )
        return None
