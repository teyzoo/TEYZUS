from typing import Dict, Any
from app.checker.telegram import (
    check_telegram
)
from app.checker.fragment import (
    check_fragment
)
from app.checker.tme import (
    check_tme
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
            "telegram": {
                "taken": None,
                "checked": False
            },
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "tme": {
                "available": None,
                "checked": False
            },
            "available": False,
            "checked": False
        }
    telegram = await check_telegram(
        username
    )
    fragment = await check_fragment(
        username
    )
    tme = await check_tme(
        username
    )
    # t.me теперь просто отражает
    # результат Telegram-проверки.
    tme = {
        "username": username,
        "available": (
            telegram.get("taken") is False
        ),
        "checked": (
            telegram.get("checked") is True
        ),
        "status": telegram.get("status")
    }
    telegram_checked = (
        telegram.get("checked") is True
    )
    telegram_free = (
        telegram.get("taken") is False
    )
    # Fragment пока НЕ является
    # подтверждённой проверкой.
    fragment_checked = (
        fragment.get("checked") is True
    )
    fragment_collectible = (
        fragment.get("collectible") is True
    )
    # Главная проверка доступности:
    #
    # Telegram должен подтвердить,
    # что username не занят.
    #
    # Fragment пока не блокирует результат,
    # потому что его реальная проверка
    # ещё не подключена.
    available = (
        telegram_checked
        and telegram_free
        and not fragment_collectible
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available,
        "checked": telegram_checked
    }
