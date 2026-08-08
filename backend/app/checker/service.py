from typing import Dict, Any
from app.checker.telegram import (
    check_telegram
)
from app.checker.fragment import (
    check_fragment
)
async def check_username(
    username: str
) -> Dict[str, Any]:
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )
    if not username:
        return {
            "username": "",
            "available": False,
            "checked": False,
            "status": "invalid"
        }
    # ---------------------------------------------------------
    # TELEGRAM
    # ---------------------------------------------------------
    telegram = await check_telegram(
        username
    )
    if telegram.get("checked") is not True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "available": False,
            "checked": False,
            "status": "telegram_not_checked"
        }
    # Username уже существует
    if telegram.get("taken") is True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "available": False,
            "checked": True,
            "status": "taken"
        }
    # ---------------------------------------------------------
    # FRAGMENT
    # ---------------------------------------------------------
    fragment = await check_fragment(
        username
    )
    # Пока Fragment реально не проверен —
    # НЕ выдаём username пользователю как свободный.
    if fragment.get("checked") is not True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": fragment,
            "available": False,
            "checked": False,
            "status": "fragment_not_checked"
        }
    # ---------------------------------------------------------
    # FINAL RESULT
    # ---------------------------------------------------------
    collectible = fragment.get(
        "collectible"
    )
    if collectible is True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": fragment,
            "available": False,
            "checked": True,
            "status": "collectible"
        }
    if (
        telegram.get("taken") is False
        and collectible is False
    ):
        return {
            "username": username,
            "telegram": telegram,
            "fragment": fragment,
            "available": True,
            "checked": True,
            "status": "available"
        }
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "available": False,
        "checked": False,
        "status": "unknown"
    }
