import asyncio
import aiohttp


TELEGRAM_URL = "https://t.me/{}"

USERNAME_TIMEOUT = aiohttp.ClientTimeout(
    total=3
)


async def check_username(
    username: str
) -> dict:

    username = (
        str(username)
        .strip()
        .lstrip("@")
        .lower()
    )

    if not username:
        return {
            "username": "",
            "available": False,
            "checked": False,
            "status": "invalid"
        }

    url = TELEGRAM_URL.format(
        username
    )

    try:

        async with aiohttp.ClientSession(
            timeout=USERNAME_TIMEOUT,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(compatible; TEYZUS/1.0)"
                )
            }
        ) as session:

            async with session.get(
                url,
                allow_redirects=True
            ) as response:

                # =============================================
                # USERNAME FOUND
                # =============================================

                if response.status == 200:

                    return {
                        "username": username,
                        "available": False,
                        "checked": True,
                        "status": "taken",
                        "verified": True
                    }

                # =============================================
                # 404
                # =============================================
                #
                # ВАЖНО:
                # 404 НЕ означает, что username свободен.
                #
                # Поэтому available=False.
                # =============================================

                if response.status == 404:

                    return {
                        "username": username,
                        "available": False,
                        "checked": False,
                        "status": "unknown",
                        "verified": False
                    }

                # =============================================
                # OTHER STATUS
                # =============================================

                return {
                    "username": username,
                    "available": False,
                    "checked": False,
                    "status": "unknown",
                    "verified": False,
                    "http_status": response.status
                }

    except asyncio.TimeoutError:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "status": "unknown",
            "verified": False,
            "error": "timeout"
        }

    except aiohttp.ClientError as exc:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "status": "unknown",
            "verified": False,
            "error": str(exc)
        }

    except Exception as exc:

        return {
            "username": username,
            "available": False,
            "checked": False,
            "status": "unknown",
            "verified": False,
            "error": str(exc)
        }
