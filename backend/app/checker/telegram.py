from typing import Dict, Any
import aiohttp
import asyncio
import re
USERNAME_RE = re.compile(
    r"^[A-Za-z][A-Za-z0-9_]{4,31}$"
)
async def check_telegram(
    username: str
) -> Dict[str, Any]:
    username = (
        str(username)
        .strip()
        .lstrip("@")
    )
    if not username:
        return {
            "username": "",
            "taken": None,
            "checked": False,
            "error": "username_required"
        }
    # Telegram username:
    # минимум 5 символов,
    # максимум 32,
    # начинается с буквы,
    # только A-Z, 0-9 и _.
    if not USERNAME_RE.fullmatch(username):
        return {
            "username": username,
            "taken": True,
            "checked": True,
            "valid": False,
            "error": "invalid_telegram_username"
        }
    url = f"https://t.me/{username}"
    timeout = aiohttp.ClientTimeout(
        total=3
    )
    try:
        async with aiohttp.ClientSession(
            timeout=timeout,
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
                status = response.status
                if status == 404:
                    return {
                        "username": username,
                        "taken": False,
                        "checked": True,
                        "valid": True,
                        "status": status
                    }
                if status == 200:
                    return {
                        "username": username,
                        "taken": True,
                        "checked": True,
                        "valid": True,
                        "status": status
                    }
                return {
                    "username": username,
                    "taken": None,
                    "checked": False,
                    "valid": True,
                    "status": status,
                    "error": "unknown_http_status"
                }
    except asyncio.TimeoutError:
        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "error": "timeout"
        }
    except aiohttp.ClientError as exc:
        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "error": str(exc)
        }
    except Exception as exc:
        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "error": str(exc)
        }
