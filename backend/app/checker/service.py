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
            "checked": False
        }
    telegram = await check_telegram(
        username
    )
    # Если Telegram не дал
    # достоверный результат —
    # username НЕ считаем свободным.
    if telegram.get(
        "checked"
    ) is not True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "available": False,
            "checked": False
        }
    # Уже занятый username
    if telegram.get(
        "taken"
    ) is True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "available": False,
            "checked": True
        }
    # Telegram показывает,
    # что username свободен.
    #
    # Fragment пока НЕ подключён,
    # поэтому не выдаём ложный available=True.
    fragment = await check_fragment(
        username
    )
    if fragment.get(
        "checked"
    ) is not True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": fragment,
            "available": False,
            "checked": False
        }
    collectible = (
        fragment.get(
            "collectible"
        )
    )
    available = (
        telegram.get("taken") is False
        and collectible is False
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "available": available,
        "checked": True
    }
