from fastapi import APIRouter

from app.checker.service import (
    check_username
)


router = APIRouter(
    prefix="/checker",
    tags=["Checker"]
)


@router.post("/")
async def checker(
    data: dict
):

    username = data.get(
        "username"
    )


    if not username:

        return {
            "error": "username required"
        }


    result = await check_username(
        username
    )


    return result
