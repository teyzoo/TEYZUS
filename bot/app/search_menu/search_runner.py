from typing import List
from app.search_menu.generator_client import generate_usernames
async def run_search(
    length: int,
    numbers: bool
) -> List[str]:
    """
    Главный запуск поиска username.
    Получает параметры поиска:
    - length — длина username
    - numbers — разрешены ли цифры
    Передаёт параметры существующему генератору
    и возвращает список найденных username.
    Проверка username выполняется отдельно через
    check_runner.py.
    """
    usernames = await generate_usernames(
        length=length,
        numbers=numbers
    )
    if not usernames:
        return []
    # Нормализуем результат генератора.
    result = []
    for username in usernames:
        if not username:
            continue
        username = str(username).strip().lstrip("@")
        if not username:
            continue
        result.append(username)
    return result
