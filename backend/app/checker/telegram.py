import asyncio
import os
import re
from typing import Dict, Any

import aiohttp


BOT_TOKEN = os.getenv("BOT_TOKEN")

TELEGRAM_API = "https://api.telegram.org"

USERNAME_RE = re.compile(
    r"^[a-zA-Z][a-zA-Z0-9_]{4,31}$"
)


async def check_telegram(
    username: str
) -> Dict[str, Any]:

    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )

    # ---------------------------------------------------------
    # BASIC VALIDATION
    # ---------------------------------------------------------

    if not username:
        return {
            "username": "",
            "taken": None,
            "checked": False,
            "valid": False,
            "status": "invalid"
        }

    if not USERNAME_RE.fullmatch(username):
        return {
            "username": username,
            "taken": None,
            "checked": True,
            "valid": False,
            "status": "invalid_username"
        }

    # ---------------------------------------------------------
    # BOT TOKEN
    # ---------------------------------------------------------

    if not BOT_TOKEN:
        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "status": "not_checked",
            "error": "bot_token_missing"
        }

    url = (
        f"{TELEGRAM_API}"
        f"/bot{BOT_TOKEN}/getChat"
    )

    timeout = aiohttp.ClientTimeout(
        total=3
    )

    try:

        async with aiohttp.ClientSession(
            timeout=timeout
        ) as session:

            async with session.get(
                url,
                params={
                    "chat_id": f"@{username}"
                }
            ) as response:

                data = await response.json(
                    content_type=None
                )

                # -------------------------------------------------
                # TELEGRAM FOUND OBJECT
                # -------------------------------------------------

                if (
                    response.status == 200
                    and data.get("ok") is True
                ):

                    result = data.get(
                        "result",
                        {}
                    )

                    return {
                        "username": username,
                        "taken": True,
                        "checked": True,
                        "valid": True,
                        "status": "taken",
                        "type": result.get("type")
                    }

                # -------------------------------------------------
                # NOT FOUND
                # -------------------------------------------------
                #
                # ВАЖНО:
                #
                # Bot API не может доказать,
                # что username свободен.
                #
                # Поэтому НЕ:
                #
                # taken=False
                #
                # а:
                #
                # taken=None
                #
                # Это защищает от ложных результатов.
                # -------------------------------------------------

                error_code = data.get(
                    "error_code"
                )

                description = data.get(
                    "description",
                    ""
                )

                if (
                    error_code == 400
                    and "not found"
                    in description.lower()
                ):

                    return {
                        "username": username,
                        "taken": None,
                        "checked": False,
                        "valid": True,
                        "status": "unknown",
                        "error": "telegram_bot_api_cannot_confirm_availability"
                    }

                # -------------------------------------------------
                # OTHER TELEGRAM ERROR
                # -------------------------------------------------

                return {
                    "username": username,
                    "taken": None,
                    "checked": False,
                    "valid": True,
                    "status": "unknown",
                    "error": description or "telegram_api_error"
                }

    except asyncio.TimeoutError:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "status": "unknown",
            "error": "timeout"
        }

    except aiohttp.ClientError as exc:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "status": "unknown",
            "error": str(exc)
        }

    except Exception as exc:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "valid": True,
            "status": "unknown",
            "error": str(exc)
        }
