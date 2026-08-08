from typing import Dict, Any
async def check_fragment(
    username: str
) -> Dict[str, Any]:
    """
    Проверка username со стороны Fragment.
    Пока реальная интеграция с Fragment API не подключена,
    мы НЕ утверждаем, что username collectible.
    Это важно, чтобы заглушка не выдавала
    ложные результаты пользователю.
    """
    username = (
        str(username)
        .strip()
        .lstrip("@")
    )
    if not username:
        return {
            "collectible": False,
            "price": None,
            "checked": False,
            "error": "username_required"
        }
    return {
        "username": username,
        "collectible": False,
        "price": None,
        "checked": False
    }
