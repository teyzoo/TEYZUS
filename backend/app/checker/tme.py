from typing import Dict, Any
import aiohttp
import asyncio
async def check_tme(
    username: str
) -> Dict[str, Any]:
    username = (
        str(username)
        .strip()
        .lstrip("@")
    )
    if not username:
        return {
            "username": "",
            "available": None,
            "checked": False,
            "error": "username_required"
        }
    url = f"https://t.me/{username}"
    timeout = aiohttp.ClientTimeout(
        total=3
    )
    try:
        async with aiohttp.ClientSession(
            timeout=timeout,
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
                if response.status == 404:
                    return {
                        "username": username,
                        "available": True,
                        "checked": True,
                        "status": 404
                    }
                if response.status == 200:
                    return {
                        "username": username,
                        "available": False,
                        "checked": True,
                        "status": 200
                    }
                return {
                    "username": username,
                    "available": None,
                    "checked": False,
                    "status": response.status,
                    "error": "unknown_http_status"
                }
    except asyncio.TimeoutError:
        return {
            "username": username,
            "available": None,
            "checked": False,
            "error": "timeout"
        }
    except aiohttp.ClientError as exc:
        return {
            "username": username,
            "available": None,
            "checked": False,
            "error": str(exc)
        }
    except Exception as exc:
        return {
            "username": username,
            "available": None,
            "checked": False,
            "error": str(exc)
        }
