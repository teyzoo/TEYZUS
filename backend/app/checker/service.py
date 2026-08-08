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
    tme = await check_tme(
        username
    )
    fragment = await check_fragment(
        username
    )
    telegram_checked = (
        telegram.get("checked") is True
    )
    tme_checked = (
        tme.get("checked") is True
    )
    telegram_free = (
        telegram.get("taken") is False
    )
    tme_free = (
        tme.get("available") is True
    )
    # Fragment пока не блокирует результат,
    # потому что реальной проверки Fragment API
    # ещё нет.
    fragment_checked = (
        fragment.get("checked") is True
    )
    fragment_collectible = (
        fragment.get("collectible") is True
    )
    available = (
        telegram_checked
        and tme_checked
        and telegram_free
        and tme_free
        and not fragment_collectible
    )
    checked = (
        telegram_checked
        and tme_checked
    )
    return {
        "username": username,
        "telegram": telegram,
        "tme": tme,
        "fragment": fragment,
        "available": available,
        "checked": checked,
        "fragment_checked": fragment_checked
    }
