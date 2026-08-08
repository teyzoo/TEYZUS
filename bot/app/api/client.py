import logging
import os
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
# HTTP SETTINGS
# ============================================================
REQUEST_TIMEOUT = aiohttp.ClientTimeout(
    total=10
)
# ============================================================
# CREATE USER
# ============================================================
async def create_user(data: dict):
    """
    Создаёт пользователя через backend.
    BACKEND_URL задаётся через переменную окружения:
        BACKEND_URL=https://your-backend.onrender.com
    Локально по умолчанию используется:
        http://localhost:8000
    Ошибка backend не должна ломать Telegram-бота.
    """
    url = f"{BACKEND_URL}/users/"
    try:
        async with aiohttp.ClientSession(
            timeout=REQUEST_TIMEOUT
        ) as session:
            async with session.post(
                url,
                json=data
            ) as response:
                # Пытаемся получить JSON независимо
                # от HTTP-кода ответа.
                try:
                    result = await response.json()
                except Exception:
                    result = {
                        "status": response.status,
                        "text": await response.text()
                    }
                if response.status >= 400:
                    logger.error(
                        "Backend returned HTTP %s for %s: %s",
                        response.status,
                        url,
                        result
                    )
                    return {
                        "success": False,
                        "status": response.status,
                        "data": result
                    }
                return {
                    "success": True,
                    "status": response.status,
                    "data": result
                }
    except asyncio.TimeoutError:
        logger.exception(
            "Backend request timeout: %s",
            url
        )
        return {
            "success": False,
            "error": "backend_timeout"
        }
    except aiohttp.ClientError:
        logger.exception(
            "Backend connection error: %s",
            url
        )
        return {
            "success": False,
            "error": "backend_connection_error"
        }
    except Exception:
        logger.exception(
            "Unexpected backend error: %s",
            url
        )
        return {
            "success": False,
            "error": "backend_unknown_error"
        }
