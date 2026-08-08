import os
import asyncio
from typing import Dict, Any

import aiohttp


BOT_TOKEN = os.getenv("BOT_TOKEN")

TELEGRAM_API = (
    "https://api.telegram.org"
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

    if not username:
        return {
            "username": "",
            "taken": None,
            "checked": False,
            "error": "username_required"
        }

    if not BOT_TOKEN:
        return {
            "username": username,
            "taken": None,
            "checked": False,
            "error": "bot_token_missing"
        }

    url = (
        f"{TELEGRAM_API}"
        f"/bot{BOT_TOKEN}/getChat"
    )

    timeout = aiohttp.ClientTimeout(
        total=2
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

                if response.status != 200:
                    return {
                        "username": username,
                        "taken": None,
                        "checked": False,
                        "status": response.status,
                        "error": "telegram_api_error"
                    }

                if data.get("ok") is True:
                    result = data.get(
                        "result",
                        {}
                    )

                    return {
                        "username": username,
                        "taken": True,
                        "checked": True,
                        "valid": True,
                        "type": result.get("type")
                    }

                error_code = data.get(
                    "error_code"
                )

                description = data.get(
                    "description",
                    ""
                )

                # Chat not found.
                #
                # Это означает, что Telegram Bot API
                # не нашёл объект с таким username.
                #
                # Но НЕ считаем это автоматически
                # 100% свободным username.
                if (
                    error_code == 400
                    and "not found" in description.lower()
                ):
                    return {
                        "username": username,
                        "taken": False,
                        "checked": True,
                        "valid": True,
                        "status": 404
                    }

                return {
                    "username": username,
                    "taken": None,
                    "checked": False,
                    "valid": True,
                    "error": description
                }

    except asyncio.TimeoutError:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "error": "timeout"
        }

    except aiohttp.ClientError as exc:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "error": str(exc)
        }

    except Exception as exc:

        return {
            "username": username,
            "taken": None,
            "checked": False,
            "error": str(exc)
        }
