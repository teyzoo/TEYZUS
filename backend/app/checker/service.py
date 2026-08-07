from app.checker.telegram import check_telegram
from app.checker.fragment import check_fragment
from app.checker.tme import check_tme



async def check_username(
    username: str
):

    telegram = await check_telegram(
        username
    )

    fragment = await check_fragment(
        username
    )

    tme = await check_tme(
        username
    )


    available = (
        not telegram["taken"]
        and not fragment["collectible"]
        and tme["available"]
    )


    return {

        "username": username,

        "telegram": telegram,

        "fragment": fragment,

        "tme": tme,

        "available": available

    }
