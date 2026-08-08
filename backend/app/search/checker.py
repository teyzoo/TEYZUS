import asyncio
import aiohttp
TELEGRAM_URL = "https://t.me/{}"
USERNAME_TIMEOUT = aiohttp.ClientTimeout(
    total=3
)
async def check_username(
    username: str
) -> dict:
    """
    Проверяет публичный Telegram username.
    ВАЖНО:
    404 означает только то, что публичная страница
    t.me не найдена.
    Это НЕ является гарантией того, что username
    можно зарегистрировать в Telegram.
    """
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )
    if not username:
        return {
            "username": username,
            "available": False,
            "status": "invalid"
        }
    url = TELEGRAM_URL.format(username)
    try:
        async with aiohttp.ClientSession(
            timeout=USERNAME_TIMEOUT,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(compatible; TEYZUS/1.0)"
                )
            }
        ) as session:
            async with session.get(
                url,
                allow_redirects=True
            ) as response:
                if response.status == 404:
                    return {
                        "username": username,
                        "available": True,
                        "status": "not_found",
                        "verified": False
                    }
                if response.status == 200:
                    return {
                        "username": username,
                        "available": False,
                        "status": "taken",
                        "verified": True
                    }
                return {
                    "username": username,
                    "available": False,
                    "status": "unknown",
                    "verified": False,
                    "http_status": response.status
                }
    except asyncio.TimeoutError:
        return {
            "username": username,
            "available": False,
            "status": "timeout",
            "verified": False
        }
    except aiohttp.ClientError:
        return {
            "username": username,
            "available": False,
            "status": "connection_error",
            "verified": False
        }
    except Exception as exc:
        return {
            "username": username,
            "available": False,
            "status": "error",
            "verified": False,
            "error": str(exc)
        }
