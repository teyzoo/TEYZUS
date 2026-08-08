from typing import Dict, Any
from app.search_menu.check_runner import run_check
async def run_search(username: str) -> Dict[str, Any]:
    """
    Проверяет конкретный username.
    Передаёт username в полный checker:
    - Telegram
    - Fragment
    - t.me
    Возвращает готовый результат проверки.
    """
    username = username.strip().lstrip("@")
    if not username:
        return {
            "username": "",
            "available": False,
            "telegram": {
                "taken": False
            },
            "fragment": {
                "collectible": False,
                "price": None
            },
            "tme": {
                "available": False
            }
        }
    return await run_check(username)
