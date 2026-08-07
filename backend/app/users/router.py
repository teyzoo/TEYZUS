from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def users_test():

    return {
        "module": "users",
        "status": "active"
    }
