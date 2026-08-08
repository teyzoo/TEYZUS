from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment
from app.checker.tme import check_tme
async def check_username(
    username: str
):
    """
    Полная проверка username.
    Проверяет:
    - Telegram
    - Fragment
    - t.me
    """
    username = (
        username
        .strip()
        .lstrip("@")
    )
    if not username:
        return {
            "username": "",
            "telegram": {
                "taken": True
            },
            "fragment": {
                "collectible": False,
                "price": None
            },
            "tme": {
                "available": False
            },
            "available": False
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
    available = (
        not telegram.get(
            "taken",
            True
        )
        and not fragment.get(
            "collectible",
            False
        )
        and tme.get(
            "available",
            False
        )
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available
    }
