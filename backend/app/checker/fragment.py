from typing import Dict, Any
async def check_fragment(
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
            "collectible": None,
            "price": None,
            "checked": False,
            "error": "username_required"
        }
    return {
        "username": username,
        "collectible": None,
        "price": None,
        "checked": False,
        "error": "fragment_not_connected"
    }
