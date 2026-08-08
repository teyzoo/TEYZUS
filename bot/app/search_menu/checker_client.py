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
    total=5
)
async def check_username(
    username: str
):
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )
    if not username:
        return None
    url = (
        f"{BACKEND_URL}"
        "/checker/"
    )
    try:
        async with aiohttp.ClientSession(
            timeout=TIMEOUT
        ) as session:
            async with session.post(
                url,
                json={
                    "username": username
                }
            ) as response:
                if response.status != 200:
                    logger.error(
                        "Checker HTTP %s: @%s",
                        response.status,
                        username
                    )
                    return None
                return await response.json()
    except asyncio.TimeoutError:
        logger.error(
            "Checker timeout: @%s",
            username
        )
        return None
    except aiohttp.ClientError as exc:
        logger.error(
            "Checker connection error @%s: %s",
            username,
            exc
        )
        return None
    except Exception as exc:
        logger.exception(
            "Checker error @%s: %s",
            username,
            exc
        )
        return None
