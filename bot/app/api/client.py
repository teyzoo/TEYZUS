import aiohttp


BACKEND_URL = "http://localhost:8000"


async def create_user(data: dict):

    async with aiohttp.ClientSession() as session:

        async with session.post(
            f"{BACKEND_URL}/users/",
            json=data
        ) as response:

            return await response.json()
