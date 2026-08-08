from typing import Dict, Any

from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment


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

    # =========================================================
    # TELEGRAM
    # =========================================================

    telegram = await check_telegram(
        username
    )

    # ---------------------------------------------------------
    # TELEGRAM НЕ ДАЛ ДОСТОВЕРНЫЙ РЕЗУЛЬТАТ
    # ---------------------------------------------------------

    if telegram.get("checked") is not True:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "status": "unknown",
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            }
        }

    # ---------------------------------------------------------
    # USERNAME ЗАНЯТ
    # ---------------------------------------------------------

    if telegram.get("taken") is True:

        return {
            "username": username,
            "available": False,
            "checked": True,
            "status": "taken",
            "telegram": telegram,
            "fragment": {
                "collectible": None,
                "price": None,
                "checked": False
            }
        }

    # =========================================================
    # FRAGMENT
    # =========================================================

    fragment = await check_fragment(
        username
    )

    # Fragment пока не подключён / не подтвердил результат.
    if fragment.get("checked") is not True:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "status": "unknown",
            "telegram": telegram,
            "fragment": fragment
        }

    collectible = fragment.get(
        "collectible"
    )

    # ---------------------------------------------------------
    # COLLECTIBLE
    # ---------------------------------------------------------

    if collectible is True:

        return {
            "username": username,
            "available": False,
            "checked": True,
            "status": "collectible",
            "telegram": telegram,
            "fragment": fragment
        }

    # ---------------------------------------------------------
    # AVAILABLE
    # ---------------------------------------------------------
    #
    # ВА
