import asyncio
import logging
import os
from typing import Dict, Any
import aiohttp
logger = logging.getLogger(__name__)
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
).rstrip("/")
TIMEOUT = aiohttp.ClientTimeout(
    total=3,
    connect=1,
    sock_connect=1,
    sock_read=2
)
async def check_username(
    username: str,
    session: aiohttp.ClientSession
) -> Dict[str, Any] | None:
    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )
    if not username:
        return None
    url = f"{BACKEND_URL}/checker/"
    try:
        async with session.post(
            url,
            json={
                "username": username
            }
        ) as response:
            if response.status != 200:
                logger.error(
                    "Checker HTTP %s for @%s",
                    response.status,
                    username
                )
                return None
            return await response.json()
    except asyncio.TimeoutError:
        logger.warning(
            "Checker timeout for @%s",
            username
        )
        return None
    except aiohttp.ClientError as exc:
        logger.warning(
            "Checker connection error for @%s: %s",
            username,
            exc
        )
        return None
    except Exception as exc:
        logger.exception(
            "Checker error for @%s",
            username
        )
        return None
