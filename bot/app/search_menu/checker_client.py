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


async def check_username(
    username: str
):

    username = (
        str(username)
        .strip()
        .lstrip("@")
    )

    if not username:
        return None

    url = f"{BACKEND_URL}/checker/"

    data = {
        "username": username
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
                        "Checker returned HTTP %s for @%s",
                        response.status,
                        username
                    )
                    return None

                return await response.json()

    except asyncio.TimeoutError:
        logger.error(
            "Checker timeout for @%s",
            username
        )
        return None

    except aiohttp.ClientError as exc:
        logger.error(
            "Checker connection error for @%s: %s",
            username,
            exc
        )
        return None

    except Exception as exc:
        logger.exception(
            "Checker error for @%s: %s",
            username,
            exc
        )
        return None
