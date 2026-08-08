from typing import Dict, Any
from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment
from app.checker.tme import check_tme
async def run_check(username: str) -> Dict[str, Any]:
    """
    Полная проверка username.
    Проверяет:
    - Telegram
    - Fragment
    - t.me
    ВАЖНО:
    Здесь не ставим результат вручную в False/True.
    Используем реальные checker-функции.
    """
    username = username.strip().lstrip("@")
    telegram = await check_telegram(username)
    fragment = await check_fragment(username)
    tme = await check_tme(username)
    available = (
        not telegram.get("taken", False)
        and not fragment.get("collectible", False)
        and tme.get("available", False)
    )
    return {
        "username": username,
        "telegram": telegram,
        "fragment": fragment,
        "tme": tme,
        "available": available
    }
