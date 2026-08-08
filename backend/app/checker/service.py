from typing import Dict, Any
from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment
from app.checker.tme import check_tme
async def check_username(
    username: str
) -> Dict[str, Any]:
    """
    Полная проверка username.
    ВАЖНО:
    Username считается доступным только тогда,
    когда все необходимые проверки действительно
    подтверждены.
    Если хотя бы одна проверка ещё не подключена
    или её результат неизвестен — available=False.
    """
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
    telegram_available = (
        telegram.get("taken") is False
    )
    fragment_available = (
        fragment.get("collectible") is False
    )
    tme_available = (
        tme.get("available") is True
    )
    all_checked = (
        telegram_checked
        and fragment_checked
        and tme_checked
    )
    available = (
        all_checked
        and telegram_available
        and fragment_available
        and tme_available
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available,
        "checked": all_checked
    }
