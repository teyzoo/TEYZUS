from typing import Dict, Any
from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment
from app.checker.tme import check_tme
async def check_username(
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
    # Если Telegram не смог подтвердить результат,
    # username не показываем пользователю как свободный.
    if telegram.get("checked") is not True:
        return {
            "username": username,
            "telegram": telegram,
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
    # Если Telegram подтвердил, что username занят,
    # дальше его бессмысленно проверять.
    if telegram.get("taken") is True:
        return {
            "username": username,
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            },
            "tme": {
                "available": False,
                "checked": False
            },
            "available": False,
            "checked": True
        }
    fragment = await check_fragment(
        username
    )
    tme = await check_tme(
        username
    )
    telegram_free = (
        telegram.get("taken") is False
    )
    tme_free = (
        tme.get("checked") is True
        and tme.get("available") is True
    )
    # Fragment пока не подтверждает состояние,
    # поэтому не используем его как положительное
    # доказательство доступности.
    fragment_confirms_taken = (
        fragment.get("checked") is True
        and fragment.get("collectible") is True
    )
    available = (
        telegram_free
        and tme_free
        and not fragment_confirms_taken
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available,
        "checked": (
            telegram.get("checked") is True
            and tme.get("checked") is True
        )
    }
