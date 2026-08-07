import aiohttp


BACKEND_URL = "http://localhost:8000"


async def search_username(
    telegram_id: str,
    query: str
):

    data = {
        "telegram_id": telegram_id,
        "query": query
    }


    async with aiohttp.ClientSession() as session:

        async with session.post(
            f"{BACKEND_URL}/search/",
            json=data
        ) as response:

            return await response.json()
