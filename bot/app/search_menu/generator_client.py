import aiohttp


BACKEND_URL = "http://localhost:8000"


async def generate_usernames(
    length: int,
    numbers: bool
):

    data = {
        "length": length,
        "numbers": numbers
    }


    async with aiohttp.ClientSession() as session:

        async with session.post(
            f"{BACKEND_URL}/generator/",
            json=data
        ) as response:

            return await response.json()
