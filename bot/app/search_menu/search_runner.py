from typing import Dict

from app.search_menu.check_runner import run_check


async def run_search(username: str) -> Dict:
    """
    Главный поиск username.

    Запускает:
    - checker
    - дополнительные источники
    - обработку результата

    Позже сюда можно добавить:
    - AI анализ
    - scoring
    - premium проверки
    - историю поиска
    """

    result = await run_check(username)

    return {
        "username": username,
        "result": result
    }
