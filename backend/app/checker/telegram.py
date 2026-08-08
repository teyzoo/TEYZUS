from typing import Dict, Any
async def check_telegram(
    username: str
) -> Dict[str, Any]:
    """
    Проверка username в Telegram.
    Пока реальная проверка Telegram API не подключена,
    функция НЕ утверждает, что username свободен.
    taken=None означает:
    результат проверки пока неизвестен.
    """
    username = (
        str(username)
        .strip()
        .lstrip("@")
    )
    if not username:
        return {
            "username": "",
            "taken": None,
            "checked": False,
            "error": "username_required"
        }
    return {
        "username": username,
        "taken": None,
        "checked": False
    }
