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
    fragment = await check_fragment(
        username
    )
    tme = await check_tme(
        username
    )
    telegram_checked = (
        telegram.get("checked") is True
    )
    fragment_checked = (
        fragment.get("checked") is True
    )
    tme_checked = (
        tme.get("checked") is True
    )
    telegram_free = (
        telegram.get("taken") is False
    )
    fragment_free = (
        fragment.get("collectible") is False
    )
    tme_free = (
        tme.get("available") is True
    )
    checked = (
        telegram_checked
        and fragment_checked
        and tme_checked
    )
    available = (
        checked
        and telegram_free
        and fragment_free
        and tme_free
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available,
        "checked": checked
    }
