from fastapi import APIRouter


from app.generator.service import (
    generate_username
)


router = APIRouter(
    prefix="/generator",
    tags=["Generator"]
)



@router.post("/")
def generator(
    data: dict
):

    length = data.get(
        "length",
        5
    )

    numbers = data.get(
        "numbers",
        False
    )


    results = generate_username(
        length,
        numbers
    )


    return {
        "results": results
    }
