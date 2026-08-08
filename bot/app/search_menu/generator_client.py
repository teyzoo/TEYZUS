import os
import aiohttp
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")
TIMEOUT = aiohttp.ClientTimeout(
    total=20
)
async def generate_usernames(
    length: int,
    numbers: bool
):
    data = {
        "length": length,
        "numbers": numbers
    }
    async with aiohttp.ClientSession(
        timeout=TIMEOUT
    ) as session:
        async with session.post(
            f"{BACKEND_URL}/generator/",
            json=data
        ) as response:
            if response.status >= 400:
                return None
            return await response.json()
