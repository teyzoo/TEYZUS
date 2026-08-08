import asyncio
import logging
import os

import aiohttp


logger = logging.getLogger(__name__)


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")


TIMEOUT = aiohttp.ClientTimeout(
    total=3
)


async def generate_usernames(
    length: int,
    numbers: bool
):

    url = f"{BACKEND_URL}/generator/"

    data = {
        "length": length,
        "numbers": numbers
    }

    try:
        async with aiohttp.ClientSession(
            timeout=TIMEOUT
        ) as session:

            async with session.post(
                url,
                json=data
            ) as response:

                if response.status != 200:
                    logger.error(
                        "Generator returned HTTP %s",
                        response.status
                    )
                    return []

                result = await response.json()

                if isinstance(result, list):
                    return result

                if isinstance(result, dict):
                    return result.get(
                        "results",
                        result.get(
                            "usernames",
                            []
                        )
                    )

                return []

    except asyncio.TimeoutError:
        logger.error(
            "Generator timeout"
        )
        return []

    except aiohttp.ClientError as exc:
        logger.error(
            "Generator connection error: %s",
            exc
        )
        return []

    except Exception as exc:
        logger.exception(
            "Generator error: %s",
            exc
        )
        return []
