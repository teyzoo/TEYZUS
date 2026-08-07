from typing import Dict


async def run_check(username: str) -> Dict:
    """
    Запускает проверку username.

    Позже сюда подключается:
    - Telegram checker
    - Fragment checker
    - T.me checker
    - дополнительные источники
    """

    result = {
        "username": username,
        "telegram": False,
        "fragment": False,
        "tme": False
    }

    return result
