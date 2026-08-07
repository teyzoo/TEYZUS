from typing import Dict


async def run_check(username: str) -> Dict:
    """
    Запускает проверку username.

    Подключаем:
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
