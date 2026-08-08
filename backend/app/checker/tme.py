from typing import Dict, Any
async def check_tme(
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
            "available": None,
            "checked": False,
            "error": "username_required"
        }
    # t.me отдельно больше не запрашиваем.
    #
    # Telegram уже проверяется в
    # check_telegram().
    #
    # Здесь результат будет установлен
    # сервисом checker/service.py.
    return {
        "username": username,
        "available": None,
        "checked": False
    }
