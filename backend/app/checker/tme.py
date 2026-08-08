from typing import Dict, Any
from app.checker.telegram import check_telegram
async def check_tme(
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
            "available": False,
            "checked": False,
            "error": "username_required"
        }
    result = await check_telegram(
        username
    )
    if result.get("checked") is not True:
        return {
            "username": username,
            "available": None,
            "checked": False,
            "error": result.get(
                "error",
                "telegram_check_failed"
            )
        }
    return {
        "username": username,
        "available": (
            result.get("taken") is False
        ),
        "checked": True,
        "status": result.get("status")
    }
