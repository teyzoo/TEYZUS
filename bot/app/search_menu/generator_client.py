import os
import aiohttp
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)
async def generate_usernames(
    length: int,
    numbers: bool
):
    """
    Запрашивает генерацию username у backend.
    BACKEND_URL берётся из переменной окружения.
    Локально по умолчанию используется localhost:8000.
    """
    data = {
        "length": length,
        "numbers": numbers
    }
    timeout = aiohttp.ClientTimeout(
        total=30
    )
    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:
        async with session.post(
            f"{BACKEND_URL}/generator/",
            json=data
        ) as response:
            response.raise_for_status()
            return await response.json()
