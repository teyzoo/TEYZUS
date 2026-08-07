from backend.app.checker.service import (
    check_username
)


async def run_check(
    usernames: list
):

    results = []


    for username in usernames:

        result = await check_username(
            username
        )

        results.append(
            result
        )


    return results
